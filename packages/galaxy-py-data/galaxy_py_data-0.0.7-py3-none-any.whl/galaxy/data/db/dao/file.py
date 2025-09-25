#  Copyright (c) 2022 bastien.saltel
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from abc import ABC,                                                    \
                abstractmethod
from sqlalchemy.sql.expression import select,                           \
                                      delete,                           \
                                      insert,                           \
                                      update
from sqlalchemy.sql.schema import Table,                                \
                                  Column,                               \
                                  PrimaryKeyConstraint,                 \
                                  ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import String,                             \
                                    Integer,                            \
                                    Boolean,                            \
                                    TIMESTAMP
from sqlalchemy.sql import bindparam
from snowflake.sqlalchemy import MergeInto

from galaxy.utils.type import Id
from galaxy.data import constant
from galaxy.data.db.db import DAO,                                      \
                              SQLAlchemyDAO,                            \
                              AsyncDAO,                                 \
                              SQLAlchemyAsyncDAO,                       \
                              SQLAlchemyDBModel,                        \
                              SQLAlchemyAsyncDBModel
from galaxy.data.model.file import Extension,                           \
                                   Format,                              \
                                   Location,                            \
                                   File,                                \
                                   EventLevel,                          \
                                   EventGroup,                          \
                                   Action,                              \
                                   Event
from galaxy.perfo.decorator import timed,                               \
                                   async_timed

class ExtensionDAO(DAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(ExtensionDAO, self).__init__()


class SQlAlchemyExtensionDAO(ExtensionDAO, SQLAlchemyDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        ExtensionDAO.__init__(self)
        SQLAlchemyDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("extension"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), Integer, nullable=False),
                                   Column(self.get_column_name("code"), String(10), nullable=False),
                                   Column(self.get_column_name("extension"), String(10), nullable=False),
                                   Column(self.get_column_name("name"), String(150), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("extension_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @timed
    def get(self, id_: int | None = None) -> Extension | dict[int, Extension] | None:
        if id_ is None:
            extensions = {}
            stmt = select(self._table)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            for row in res:
                extension = Extension(getattr(row, self.get_column_name("id")))
                extension.code = getattr(row, self.get_column_name("code"))
                extension.extension = getattr(row, self.get_column_name("extension"))
                extension.name = getattr(row, self.get_column_name("name"))
                extensions[extension.id] = extension
            return extensions
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == id_)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            row = res.first()
            extension = None
            if row is not None:
                extension = Extension(getattr(row, self.get_column_name("id")))
                extension.code = getattr(row, self.get_column_name("code"))
                extension.extension = getattr(row, self.get_column_name("extension"))
                extension.name = getattr(row, self.get_column_name("name"))
            return extension

    @timed
    def create(self, extensions: list[Extension]) -> None:
        if len(extensions) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): extension.id,
                                                self.get_column_name("code"): extension.code,
                                                self.get_column_name("extension"): extension.extension,
                                                self.get_column_name("name"): extension.name
                                               } for extension in extensions])
            with self._engine.begin() as conn:
                conn.execute(stmt)

    @timed
    def update(self, extensions: list[Extension]) -> None:
        if len(extensions) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("code"): bindparam("code"),
                                                                                                                             self.get_column_name("extension"): bindparam("extension"),
                                                                                                                             self.get_column_name("name"): bindparam("name")
                                                                                                                            })
            with self._engine.begin() as conn:
                conn.execute(stmt, [{
                                     "_id": extension.id,
                                     "code": extension.code,
                                     "extension": extension.extension,
                                     "name": extension.name
                                    } for extension in extensions])

    @timed
    def delete(self, extensions: list[Extension]) -> None:
        if len(extensions) > 0:
            ids = [extension.id for extension in extensions]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            with self._engine.begin() as conn:
                conn.execute(stmt)


class ExtensionAsyncDAO(AsyncDAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(ExtensionAsyncDAO, self).__init__()


class SQlAlchemyExtensionAsyncDAO(ExtensionAsyncDAO, SQLAlchemyAsyncDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        ExtensionAsyncDAO.__init__(self)
        SQLAlchemyAsyncDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("extension"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), Integer, nullable=False),
                                   Column(self.get_column_name("code"), String(10), nullable=False),
                                   Column(self.get_column_name("extension"), String(10), nullable=False),
                                   Column(self.get_column_name("name"), String(150), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("extension_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @async_timed
    async def get(self, id_: int | None = None) -> Extension | dict[int, Extension] | None:
        if id_ is None:
            extensions = {}
            stmt = select(self._table)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            for row in res:
                extension = Extension(getattr(row, self.get_column_name("id")))
                extension.code = getattr(row, self.get_column_name("code"))
                extension.extension = getattr(row, self.get_column_name("extension"))
                extension.name = getattr(row, self.get_column_name("name"))
                extensions[extension.id] = extension
            return extensions
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == id_)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            row = res.first()
            extension = None
            if row is not None:
                extension = Extension(getattr(row, self.get_column_name("id")))
                extension.code = getattr(row, self.get_column_name("code"))
                extension.extension = getattr(row, self.get_column_name("extension"))
                extension.name = getattr(row, self.get_column_name("name"))
            return extension

    @async_timed
    async def create(self, extensions: list[Extension]) -> None:
        if len(extensions) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): extension.id,
                                                self.get_column_name("code"): extension.code,
                                                self.get_column_name("extension"): extension.extension,
                                                self.get_column_name("name"): extension.name
                                               } for extension in extensions])
            async with self._engine.begin() as conn:
                await conn.execute(stmt)

    @async_timed
    async def update(self, extensions: list[Extension]) -> None:
        if len(extensions) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("code"): bindparam("code"),
                                                                                                                             self.get_column_name("extension"): bindparam("extension"),
                                                                                                                             self.get_column_name("name"): bindparam("name")
                                                                                                                            })
            async with self._engine.begin() as conn:
                await conn.execute(stmt, [{
                                           "_id": extension.id,
                                           "code": extension.code,
                                           "extension": extension.extension,
                                           "name": extension.name
                                          } for extension in extensions])

    @async_timed
    async def delete(self, extensions: list[Extension]) -> None:
        if len(extensions) > 0:
            ids = [extension.id for extension in extensions]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            async with self._engine.begin() as conn:
                await conn.execute(stmt)


class FormatDAO(DAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(FormatDAO, self).__init__()


class SQlAlchemyFormatDAO(FormatDAO, SQLAlchemyDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        FormatDAO.__init__(self)
        SQLAlchemyDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("format"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), Integer, nullable=False),
                                   Column(self.get_column_name("code"), String(15), nullable=False),
                                   Column(self.get_column_name("name"), String(80), nullable=False),
                                   Column(self.get_column_name("fullname"), String(120), nullable=False),
                                   Column(self.get_column_name("is_proprietary"), Boolean, nullable=False),
                                   Column(self.get_column_name("create_by"), String(150), nullable=True),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("format_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @timed
    def get(self, id_: int | None = None) -> Format | dict[int, Format] | None:
        if id_ is None:
            formats = {}
            stmt = select(self._table)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            for row in res:
                format = Format(getattr(row, self.get_column_name("id")))
                format.code = getattr(row, self.get_column_name("code"))
                format.name = getattr(row, self.get_column_name("name"))
                format.fullname = getattr(row, self.get_column_name("fullname"))
                format.is_proprietary = getattr(row, self.get_column_name("is_proprietary"))
                format.create_by = getattr(row, self.get_column_name("create_by"))
                formats[format.id] = format
            return formats
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == id_)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            row = res.first()
            format = None
            if row is not None:
                format = Format(getattr(row, self.get_column_name("id")))
                format.code = getattr(row, self.get_column_name("code"))
                format.name = getattr(row, self.get_column_name("name"))
                format.fullname = getattr(row, self.get_column_name("fullname"))
                format.is_proprietary = getattr(row, self.get_column_name("is_proprietary"))
                format.create_by = getattr(row, self.get_column_name("create_by"))
            return format

    @timed
    def create(self, formats: list[Format]) -> None:
        if len(formats) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): format.id,
                                                self.get_column_name("code"): format.code,
                                                self.get_column_name("name"): format.name,
                                                self.get_column_name("fullname"): format.fullname,
                                                self.get_column_name("is_proprietary"): format.is_proprietary,
                                                self.get_column_name("create_by"): format.create_by
                                               } for format in formats])
            with self._engine.begin() as conn:
                conn.execute(stmt)

    @timed
    def update(self, formats: list[Format]) -> None:
        if len(formats) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("code"): bindparam("code"),
                                                                                                                             self.get_column_name("name"): bindparam("name"),
                                                                                                                             self.get_column_name("fullname"): bindparam("fullname"),
                                                                                                                             self.get_column_name("is_proprietary"): bindparam("is_proprietary"),
                                                                                                                             self.get_column_name("create_by"): bindparam("create_by")
                                                                                                                            })
            with self._engine.begin() as conn:
                conn.execute(stmt, [{
                                     "_id": format.id,
                                     "code": format.code,
                                     "name": format.name,
                                     "fullname": format.fullname,
                                     "is_proprietary": format.is_proprietary,
                                     "create_by": format.create_by
                                    } for format in formats])

    @timed
    def delete(self, formats: list[Format]) -> None:
        if len(formats) > 0:
            ids = [format.id for format in formats]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            with self._engine.begin() as conn:
                conn.execute(stmt)


class FormatAsyncDAO(AsyncDAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(FormatAsyncDAO, self).__init__()


class SQlAlchemyFormatAsyncDAO(FormatAsyncDAO, SQLAlchemyAsyncDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        FormatAsyncDAO.__init__(self)
        SQLAlchemyAsyncDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("format"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), Integer, nullable=False),
                                   Column(self.get_column_name("code"), String(15), nullable=False),
                                   Column(self.get_column_name("name"), String(80), nullable=False),
                                   Column(self.get_column_name("fullname"), String(120), nullable=False),
                                   Column(self.get_column_name("is_proprietary"), Boolean, nullable=False),
                                   Column(self.get_column_name("create_by"), String(150), nullable=True),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("format_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @async_timed
    async def get(self, id_: int | None = None) -> Format | dict[int, Format] | None:
        if id_ is None:
            formats = {}
            stmt = select(self._table)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            for row in res:
                format = Format(getattr(row, self.get_column_name("id")))
                format.code = getattr(row, self.get_column_name("code"))
                format.name = getattr(row, self.get_column_name("name"))
                format.fullname = getattr(row, self.get_column_name("fullname"))
                format.is_proprietary = getattr(row, self.get_column_name("is_proprietary"))
                format.create_by = getattr(row, self.get_column_name("create_by"))
                formats[format.id] = format
            return formats
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == id_)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            row = res.first()
            format = None
            if row is not None:
                format = Format(getattr(row, self.get_column_name("id")))
                format.code = getattr(row, self.get_column_name("code"))
                format.name = getattr(row, self.get_column_name("name"))
                format.fullname = getattr(row, self.get_column_name("fullname"))
                format.is_proprietary = getattr(row, self.get_column_name("is_proprietary"))
                format.create_by = getattr(row, self.get_column_name("create_by"))
            return format

    @async_timed
    async def create(self, formats: list[Format]) -> None:
        if len(formats) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): format.id,
                                                self.get_column_name("code"): format.code,
                                                self.get_column_name("name"): format.name,
                                                self.get_column_name("fullname"): format.fullname,
                                                self.get_column_name("is_proprietary"): format.is_proprietary,
                                                self.get_column_name("create_by"): format.create_by
                                               } for format in formats])
            async with self._engine.begin() as conn:
                await conn.execute(stmt)

    @async_timed
    async def update(self, formats: list[Format]) -> None:
        if len(formats) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("code"): bindparam("code"),
                                                                                                                             self.get_column_name("name"): bindparam("name"),
                                                                                                                             self.get_column_name("fullname"): bindparam("fullname"),
                                                                                                                             self.get_column_name("is_proprietary"): bindparam("is_proprietary"),
                                                                                                                             self.get_column_name("create_by"): bindparam("create_by")
                                                                                                                            })
            async with self._engine.begin() as conn:
                await conn.execute(stmt, [{
                                           "_id": format.id,
                                           "code": format.code,
                                           "name": format.name,
                                           "fullname": format.fullname,
                                           "is_proprietary": format.is_proprietary,
                                           "create_by": format.create_by
                                          } for format in formats])

    @async_timed
    async def delete(self, formats: list[Format]) -> None:
        if len(formats) > 0:
            ids = [format.id for format in formats]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            async with self._engine.begin() as conn:
                await conn.execute(stmt)


class LocationDAO(DAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(LocationDAO, self).__init__()


class SQlAlchemyLocationDAO(LocationDAO, SQLAlchemyDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        LocationDAO.__init__(self)
        SQLAlchemyDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("location"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                                   Column(self.get_column_name("path"), String(250), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("location_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @timed
    def get(self, id_: Id | None = None) -> Location | dict[Id, Location] | None:
        if id_ is None:
            locations = {}
            stmt = select(self._table)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            for row in res:
                location = Location(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                location.path = getattr(row, self.get_column_name("path"))
                locations[location.id] = location
            return locations
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == self.get_uuid_from_model(id_))
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            row = res.first()
            location = None
            if row is not None:
                location = Location(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                location.path = getattr(row, self.get_column_name("path"))
            return location

    @timed
    def create(self, locations: list[Location]) -> None:
        if len(locations) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): self.get_uuid_from_model(location.id),
                                                self.get_column_name("path"): location.path
                                               } for location in locations])
            with self._engine.begin() as conn:
                conn.execute(stmt)

    @timed
    def update(self, locations: list[Location]) -> None:
        if len(locations) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("path"): bindparam("path")
                                                                                                                            })
            with self._engine.begin() as conn:
                conn.execute(stmt, [{
                                     "_id": self.get_uuid_from_model(location.id),
                                     "path": location.path
                                    } for location in locations])

    @timed
    def delete(self, locations: list[Location]) -> None:
        if len(locations) > 0:
            ids = [self.get_uuid_from_model(location.id) for location in locations]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            with self._engine.begin() as conn:
                conn.execute(stmt)


class SnowflakeSQlAlchemyLocationDAO(SQlAlchemyLocationDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(SnowflakeSQlAlchemyLocationDAO, self).__init__()

    @timed
    def upsert(self, locations: list[Location]) -> None:
        if len(locations) > 0:
            temp_table = Table(self.get_table_name("{}location".format(constant.TEMP_TABLE_PREFIX)),
                               self._metadata,
                               Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                               Column(self.get_column_name("path"), String(250), nullable=False),
                               *(self.get_meta_columns()),
                               schema=constant.TEMP_SCHEMA,
                               keep_existing=True)
            temp_table.create(self._engine)
            stmt = insert(temp_table).values([{
                                               self.get_column_name("id"): self.get_uuid_from_model(location.id),
                                               self.get_column_name("path"): location.path
                                              } for location in locations])
            with self._engine.begin() as conn:
                conn.execute(stmt)

            merge = MergeInto(target=self._table,
                              source=temp_table,
                              on=(getattr(self._table.c, self.get_column_name("id")) == getattr(temp_table.c, self.get_column_name("id"))))
            val = {
                   self.get_column_name("path"): getattr(temp_table.c, self.get_column_name("path"))
                  }
            merge.when_matched_then_update().values(**val)
            val[self.get_column_name("id")] = getattr(temp_table.c, self.get_column_name("id"))
            merge.when_not_matched_then_insert().values(**val)
            with self._engine.begin() as conn:
                conn.execute(merge)

            temp_table.drop(self._engine)


class LocationAsyncDAO(AsyncDAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(LocationAsyncDAO, self).__init__()


class SQlAlchemyLocationAsyncDAO(LocationAsyncDAO, SQLAlchemyAsyncDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        LocationAsyncDAO.__init__(self)
        SQLAlchemyAsyncDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("location"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                                   Column(self.get_column_name("path"), String(250), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("location_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @async_timed
    async def get(self, id_: Id | None = None) -> Location | dict[Id, Location] | None:
        if id_ is None:
            locations = {}
            stmt = select(self._table)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            for row in res:
                location = Location(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                location.path = getattr(row, self.get_column_name("path"))
                locations[location.id] = location
            return locations
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == self.get_uuid_from_model(id_))
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            row = res.first()
            location = None
            if row is not None:
                location = Location(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                location.path = getattr(row, self.get_column_name("path"))
            return location

    @async_timed
    async def create(self, locations: list[Location]) -> None:
        if len(locations) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): self.get_uuid_from_model(location.id),
                                                self.get_column_name("path"): location.path
                                               } for location in locations])
            async with self._engine.begin() as conn:
                await conn.execute(stmt)

    @async_timed
    async def update(self, locations: list[Location]) -> None:
        if len(locations) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("path"): bindparam("path")
                                                                                                                            })
            async with self._engine.begin() as conn:
                await conn.execute(stmt, [{
                                           "_id": self.get_uuid_from_model(location.id),
                                           "path": location.path
                                          } for location in locations])

    @async_timed
    async def delete(self, locations: list[Location]) -> None:
        if len(locations) > 0:
            ids = [self.get_uuid_from_model(location.id) for location in locations]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            async with self._engine.begin() as conn:
                await conn.execute(stmt)


class SnowflakeSQlAlchemyLocationAsyncDAO(SQlAlchemyLocationAsyncDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(SnowflakeSQlAlchemyLocationAsyncDAO, self).__init__()

    @async_timed
    async def upsert(self, locations: list[Location]) -> None:
        if len(locations) > 0:
            temp_table = Table(self.get_table_name("{}location".format(constant.TEMP_TABLE_PREFIX)),
                               self._metadata,
                               Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                               Column(self.get_column_name("path"), String(250), nullable=False),
                               *(self.get_meta_columns()),
                               schema=constant.TEMP_SCHEMA,
                               keep_existing=True)
            temp_table.create(self._engine)
            stmt = insert(temp_table).values([{
                                               self.get_column_name("id"): self.get_uuid_from_model(location.id),
                                               self.get_column_name("path"): location.path
                                              } for location in locations])
            async with self._engine.begin() as conn:
                await conn.execute(stmt)

            merge = MergeInto(target=self._table,
                              source=temp_table,
                              on=(getattr(self._table.c, self.get_column_name("id")) == getattr(temp_table.c, self.get_column_name("id"))))
            val = {
                   self.get_column_name("path"): getattr(temp_table.c, self.get_column_name("path"))
                  }
            merge.when_matched_then_update().values(**val)
            val[self.get_column_name("id")] = getattr(temp_table.c, self.get_column_name("id"))
            merge.when_not_matched_then_insert().values(**val)
            async with self._engine.begin() as conn:
                await conn.execute(merge)

            temp_table.drop(self._engine)


class FileDAO(DAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(FileDAO, self).__init__()


class SQlAlchemyFileDAO(FileDAO, SQLAlchemyDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        FileDAO.__init__(self)
        SQLAlchemyDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("file"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                                   Column(self.get_column_name("name"), String(150), nullable=False),
                                   Column(self.get_column_name("path_id"), self.get_uuid_type(), nullable=False),
                                   Column(self.get_column_name("extension_id"), Integer, nullable=False),
                                   Column(self.get_column_name("format_id"), Integer, nullable=False),
                                   Column(self.get_column_name("create_date"), TIMESTAMP(timezone=True), nullable=False),
                                   Column(self.get_column_name("create_by"), String(50), nullable=False),
                                   Column(self.get_column_name("last_modif_date"), TIMESTAMP(timezone=True), nullable=False),
                                   Column(self.get_column_name("last_modif_by"), String(50), nullable=False),
                                   Column(self.get_column_name("delete_date"), TIMESTAMP(timezone=True), nullable=True),
                                   Column(self.get_column_name("delete_by"), String(50), nullable=True),
                                   Column(self.get_column_name("is_readable"), Boolean, nullable=False),
                                   Column(self.get_column_name("is_writeable"), Boolean, nullable=False),
                                   Column(self.get_column_name("is_executable"), Boolean, nullable=False),
                                   Column(self.get_column_name("posix_permission"), String(4), nullable=True),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("file_pk")),
                                   ForeignKeyConstraint([self.get_column_name("path_id")],
                                                        ["{}.{}".format(self.get_table_name("location", "file"), self.get_column_name("id"))],
                                                        name=self.get_key_name("file_fk1")),
                                   ForeignKeyConstraint([self.get_column_name("extension_id")],
                                                        ["{}.{}".format(self.get_table_name("extension", "file"), self.get_column_name("id"))],
                                                        name=self.get_key_name("file_fk2")),
                                   ForeignKeyConstraint([self.get_column_name("format_id")],
                                                        ["{}.{}".format(self.get_table_name("format", "file"), self.get_column_name("id"))],
                                                        name=self.get_key_name("file_fk3")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @timed
    def get(self, id_: Id | None = None) -> File | dict[Id, File] | None:
        if id_ is None:
            files = {}
            stmt = select(self._table)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            for row in res:
                file = File(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                file.name = getattr(row, self.get_column_name("name"))
                file.path_id = Id(self.get_uuid_from_db(getattr(row, self.get_column_name("path_id"))))
                file.extension_id = getattr(row, self.get_column_name("extension_id"))
                file.format_id = getattr(row, self.get_column_name("format_id"))
                file.create_date = getattr(row, self.get_column_name("create_date"))
                file.create_by = getattr(row, self.get_column_name("create_by"))
                file.last_modif_date = getattr(row, self.get_column_name("last_modif_date"))
                file.last_modif_by = getattr(row, self.get_column_name("last_modif_by"))
                file.delete_date = getattr(row, self.get_column_name("delete_date"))
                file.delete_by = getattr(row, self.get_column_name("delete_by"))
                file.is_readable = getattr(row, self.get_column_name("is_readable"))
                file.is_writeable = getattr(row, self.get_column_name("is_writeable"))
                file.is_executable = getattr(row, self.get_column_name("is_executable"))
                file.posix_permission = getattr(row, self.get_column_name("posix_permission"))
                files[file.id] = file
            return files
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == self.get_uuid_from_model(id_))
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            row = res.first()
            file = None
            if row is not None:
                file = File(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                file.name = getattr(row, self.get_column_name("name"))
                file.path_id = Id(self.get_uuid_from_db(getattr(row, self.get_column_name("path_id"))))
                file.extension_id = getattr(row, self.get_column_name("extension_id"))
                file.format_id = getattr(row, self.get_column_name("format_id"))
                file.create_date = getattr(row, self.get_column_name("create_date"))
                file.create_by = getattr(row, self.get_column_name("create_by"))
                file.last_modif_date = getattr(row, self.get_column_name("last_modif_date"))
                file.last_modif_by = getattr(row, self.get_column_name("last_modif_by"))
                file.delete_date = getattr(row, self.get_column_name("delete_date"))
                file.delete_by = getattr(row, self.get_column_name("delete_by"))
                file.is_readable = getattr(row, self.get_column_name("is_readable"))
                file.is_writeable = getattr(row, self.get_column_name("is_writeable"))
                file.is_executable = getattr(row, self.get_column_name("is_executable"))
                file.posix_permission = getattr(row, self.get_column_name("posix_permission"))
            return file

    @timed
    def create(self, files: list[File]) -> None:
        if len(files) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): self.get_uuid_from_model(file.id),
                                                self.get_column_name("name"): file.name,
                                                self.get_column_name("path_id"): self.get_uuid_from_model(file.path_id),
                                                self.get_column_name("extension_id"): file.extension_id,
                                                self.get_column_name("format_id"): file.format_id,
                                                self.get_column_name("create_date"): file.create_date,
                                                self.get_column_name("create_by"): file.create_by,
                                                self.get_column_name("last_modif_date"): file.last_modif_date,
                                                self.get_column_name("last_modif_by"): file.last_modif_by,
                                                self.get_column_name("delete_date"): file.delete_date,
                                                self.get_column_name("delete_by"): file.delete_by,
                                                self.get_column_name("is_readable"): file.is_readable,
                                                self.get_column_name("is_writeable"): file.is_writeable,
                                                self.get_column_name("is_executable"): file.is_executable,
                                                self.get_column_name("posix_permission"): file.posix_permission
                                               } for file in files])
            with self._engine.begin() as conn:
                conn.execute(stmt)

    @timed
    def update(self, files: list[File]) -> None:
        if len(files) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("name"): bindparam("name"),
                                                                                                                             self.get_column_name("path_id"): bindparam("path_id"),
                                                                                                                             self.get_column_name("extension_id"): bindparam("extension_id"),
                                                                                                                             self.get_column_name("format_id"): bindparam("format_id"),
                                                                                                                             self.get_column_name("create_date"): bindparam("create_date"),
                                                                                                                             self.get_column_name("create_by"): bindparam("create_by"),
                                                                                                                             self.get_column_name("last_modif_date"): bindparam("last_modif_date"),
                                                                                                                             self.get_column_name("last_modif_by"): bindparam("last_modif_by"),
                                                                                                                             self.get_column_name("delete_date"): bindparam("delete_date"),
                                                                                                                             self.get_column_name("delete_by"): bindparam("delete_by"),
                                                                                                                             self.get_column_name("is_readable"): bindparam("is_readable"),
                                                                                                                             self.get_column_name("is_writeable"): bindparam("is_writeable"),
                                                                                                                             self.get_column_name("is_executable"): bindparam("is_executable"),
                                                                                                                             self.get_column_name("posix_permission"): bindparam("posix_permission")
                                                                                                                            })
            with self._engine.begin() as conn:
                conn.execute(stmt, [{
                                     "_id": self.get_uuid_from_model(file.id),
                                     "name": file.name,
                                     "path_id": self.get_uuid_from_model(file.path_id),
                                     "extension_id": file.extension_id,
                                     "format_id": file.format_id,
                                     "create_date": file.create_date,
                                     "create_by": file.create_by,
                                     "last_modif_date": file.last_modif_date,
                                     "last_modif_by": file.last_modif_by,
                                     "delete_date": file.delete_date,
                                     "delete_by": file.delete_by,
                                     "is_readable": file.is_readable,
                                     "is_writeable": file.is_writeable,
                                     "is_executable": file.is_executable,
                                     "posix_permission": file.posix_permission
                                    } for file in files])

    @timed
    def delete(self, files: list[File]) -> None:
        if len(files) > 0:
            ids = [self.get_uuid_from_model(file.id) for file in files]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            with self._engine.begin() as conn:
                conn.execute(stmt)


class SnowflakeSQlAlchemyFileDAO(SQlAlchemyFileDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(SnowflakeSQlAlchemyFileDAO, self).__init__()

    @timed
    def upsert(self, files: list[File]) -> None:
        if len(files) > 0:
            temp_table = Table(self.get_table_name("{}file".format(constant.TEMP_TABLE_PREFIX)),
                               self._metadata,
                           Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                               Column(self.get_column_name("name"), String(150), nullable=False),
                               Column(self.get_column_name("path_id"), self.get_uuid_type(), nullable=False),
                               Column(self.get_column_name("extension_id"), Integer, nullable=False),
                               Column(self.get_column_name("format_id"), Integer, nullable=False),
                               Column(self.get_column_name("create_date"), TIMESTAMP(timezone=True), nullable=False),
                               Column(self.get_column_name("create_by"), String(50), nullable=False),
                               Column(self.get_column_name("last_modif_date"), TIMESTAMP(timezone=True), nullable=False),
                               Column(self.get_column_name("last_modif_by"), String(50), nullable=False),
                               Column(self.get_column_name("delete_date"), TIMESTAMP(timezone=True), nullable=True),
                               Column(self.get_column_name("delete_by"), String(50), nullable=True),
                               Column(self.get_column_name("is_readable"), Boolean, nullable=False),
                               Column(self.get_column_name("is_writeable"), Boolean, nullable=False),
                               Column(self.get_column_name("is_executable"), Boolean, nullable=False),
                               Column(self.get_column_name("posix_permission"), String(4), nullable=True),
                               *(self.get_meta_columns()),
                               schema=constant.TEMP_SCHEMA,
                               keep_existing=True)
            temp_table.create(self._engine)
            stmt = insert(temp_table).values([{
                                               self.get_column_name("id"): self.get_uuid_from_model(file.id),
                                               self.get_column_name("name"): file.name,
                                               self.get_column_name("path_id"): self.get_uuid_from_model(file.path_id),
                                               self.get_column_name("extension_id"): file.extension_id,
                                               self.get_column_name("format_id"): file.format_id,
                                               self.get_column_name("create_date"): file.create_date,
                                               self.get_column_name("create_by"): file.create_by,
                                               self.get_column_name("last_modif_date"): file.last_modif_date,
                                               self.get_column_name("last_modif_by"): file.last_modif_by,
                                               self.get_column_name("delete_date"): file.delete_date,
                                               self.get_column_name("delete_by"): file.delete_by,
                                               self.get_column_name("is_readable"): file.is_readable,
                                               self.get_column_name("is_writeable"): file.is_writeable,
                                               self.get_column_name("is_executable"): file.is_executable,
                                               self.get_column_name("posix_permission"): file.posix_permission
                                              } for file in files])
            with self._engine.begin() as conn:
                conn.execute(stmt)

            merge = MergeInto(target=self._table,
                              source=temp_table,
                              on=(getattr(self._table.c, self.get_column_name("id")) == getattr(temp_table.c, self.get_column_name("id"))))
            val = {
                   self.get_column_name("name"): getattr(temp_table.c, self.get_column_name("name")),
                   self.get_column_name("path_id"): getattr(temp_table.c, self.get_column_name("path_id")),
                   self.get_column_name("extension_id"): getattr(temp_table.c, self.get_column_name("extension_id")),
                   self.get_column_name("format_id"): getattr(temp_table.c, self.get_column_name("format_id")),
                   self.get_column_name("create_date"): getattr(temp_table.c, self.get_column_name("create_date")),
                   self.get_column_name("create_by"): getattr(temp_table.c, self.get_column_name("create_by")),
                   self.get_column_name("last_modif_date"): getattr(temp_table.c, self.get_column_name("last_modif_date")),
                   self.get_column_name("last_modif_by"): getattr(temp_table.c, self.get_column_name("last_modif_by")),
                   self.get_column_name("delete_date"): getattr(temp_table.c, self.get_column_name("delete_date")),
                   self.get_column_name("delete_by"): getattr(temp_table.c, self.get_column_name("delete_by")),
                   self.get_column_name("is_readable"): getattr(temp_table.c, self.get_column_name("is_readable")),
                   self.get_column_name("is_writeable"): getattr(temp_table.c, self.get_column_name("is_writeable")),
                   self.get_column_name("is_executable"): getattr(temp_table.c, self.get_column_name("is_executable")),
                   self.get_column_name("posix_permission"): getattr(temp_table.c, self.get_column_name("posix_permission"))
                  }
            merge.when_matched_then_update().values(**val)
            val[self.get_column_name("id")] = getattr(temp_table.c, self.get_column_name("id"))
            merge.when_not_matched_then_insert().values(**val)
            with self._engine.begin() as conn:
                conn.execute(merge)

            temp_table.drop(self._engine)


class FileAsyncDAO(AsyncDAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(FileAsyncDAO, self).__init__()


class SQlAlchemyFileAsyncDAO(FileAsyncDAO, SQLAlchemyAsyncDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        FileAsyncDAO.__init__(self)
        SQLAlchemyAsyncDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("file"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                                   Column(self.get_column_name("name"), String(150), nullable=False),
                                   Column(self.get_column_name("path_id"), self.get_uuid_type(), nullable=False),
                                   Column(self.get_column_name("extension_id"), Integer, nullable=False),
                                   Column(self.get_column_name("format_id"), Integer, nullable=False),
                                   Column(self.get_column_name("create_date"), TIMESTAMP(timezone=True), nullable=False),
                                   Column(self.get_column_name("create_by"), String(50), nullable=False),
                                   Column(self.get_column_name("last_modif_date"), TIMESTAMP(timezone=True), nullable=False),
                                   Column(self.get_column_name("last_modif_by"), String(50), nullable=False),
                                   Column(self.get_column_name("delete_date"), TIMESTAMP(timezone=True), nullable=True),
                                   Column(self.get_column_name("delete_by"), String(50), nullable=True),
                                   Column(self.get_column_name("is_readable"), Boolean, nullable=False),
                                   Column(self.get_column_name("is_writeable"), Boolean, nullable=False),
                                   Column(self.get_column_name("is_executable"), Boolean, nullable=False),
                                   Column(self.get_column_name("posix_permission"), String(4), nullable=True),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("file_pk")),
                                   ForeignKeyConstraint([self.get_column_name("path_id")],
                                                        ["{}.{}".format(self.get_table_name("location", "file"), self.get_column_name("id"))],
                                                        name=self.get_key_name("file_fk1")),
                                   ForeignKeyConstraint([self.get_column_name("extension_id")],
                                                        ["{}.{}".format(self.get_table_name("extension", "file"), self.get_column_name("id"))],
                                                        name=self.get_key_name("file_fk2")),
                                   ForeignKeyConstraint([self.get_column_name("format_id")],
                                                        ["{}.{}".format(self.get_table_name("format", "file"), self.get_column_name("id"))],
                                                        name=self.get_key_name("file_fk3")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @async_timed
    async def get(self, id_: Id | None = None) -> File | dict[Id, File] | None:
        if id_ is None:
            files = {}
            stmt = select(self._table)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            for row in res:
                file = File(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                file.name = getattr(row, self.get_column_name("name"))
                file.path_id = Id(self.get_uuid_from_db(getattr(row, self.get_column_name("path_id"))))
                file.extension_id = getattr(row, self.get_column_name("extension_id"))
                file.format_id = getattr(row, self.get_column_name("format_id"))
                file.create_date = getattr(row, self.get_column_name("create_date"))
                file.create_by = getattr(row, self.get_column_name("create_by"))
                file.last_modif_date = getattr(row, self.get_column_name("last_modif_date"))
                file.last_modif_by = getattr(row, self.get_column_name("last_modif_by"))
                file.delete_date = getattr(row, self.get_column_name("delete_date"))
                file.delete_by = getattr(row, self.get_column_name("delete_by"))
                file.is_readable = getattr(row, self.get_column_name("is_readable"))
                file.is_writeable = getattr(row, self.get_column_name("is_writeable"))
                file.is_executable = getattr(row, self.get_column_name("is_executable"))
                file.posix_permission = getattr(row, self.get_column_name("posix_permission"))
                files[file.id] = file
            return files
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == self.get_uuid_from_model(id_))
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            row = res.first()
            file = None
            if row is not None:
                file = File(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                file.name = getattr(row, self.get_column_name("name"))
                file.path_id = Id(self.get_uuid_from_db(getattr(row, self.get_column_name("path_id"))))
                file.extension_id = getattr(row, self.get_column_name("extension_id"))
                file.format_id = getattr(row, self.get_column_name("format_id"))
                file.create_date = getattr(row, self.get_column_name("create_date"))
                file.create_by = getattr(row, self.get_column_name("create_by"))
                file.last_modif_date = getattr(row, self.get_column_name("last_modif_date"))
                file.last_modif_by = getattr(row, self.get_column_name("last_modif_by"))
                file.delete_date = getattr(row, self.get_column_name("delete_date"))
                file.delete_by = getattr(row, self.get_column_name("delete_by"))
                file.is_readable = getattr(row, self.get_column_name("is_readable"))
                file.is_writeable = getattr(row, self.get_column_name("is_writeable"))
                file.is_executable = getattr(row, self.get_column_name("is_executable"))
                file.posix_permission = getattr(row, self.get_column_name("posix_permission"))
            return file

    @async_timed
    async def create(self, files: list[File]) -> None:
        if len(files) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): self.get_uuid_from_model(file.id),
                                                self.get_column_name("name"): file.name,
                                                self.get_column_name("path_id"): self.get_uuid_from_model(file.path_id),
                                                self.get_column_name("extension_id"): file.extension_id,
                                                self.get_column_name("format_id"): file.format_id,
                                                self.get_column_name("create_date"): file.create_date,
                                                self.get_column_name("create_by"): file.create_by,
                                                self.get_column_name("last_modif_date"): file.last_modif_date,
                                                self.get_column_name("last_modif_by"): file.last_modif_by,
                                                self.get_column_name("delete_date"): file.delete_date,
                                                self.get_column_name("delete_by"): file.delete_by,
                                                self.get_column_name("is_readable"): file.is_readable,
                                                self.get_column_name("is_writeable"): file.is_writeable,
                                                self.get_column_name("is_executable"): file.is_executable,
                                                self.get_column_name("posix_permission"): file.posix_permission
                                               } for file in files])
            async with self._engine.begin() as conn:
                await conn.execute(stmt)

    @async_timed
    async def update(self, files: list[File]) -> None:
        if len(files) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("name"): bindparam("name"),
                                                                                                                             self.get_column_name("path_id"): bindparam("path_id"),
                                                                                                                             self.get_column_name("extension_id"): bindparam("extension_id"),
                                                                                                                             self.get_column_name("format_id"): bindparam("format_id"),
                                                                                                                             self.get_column_name("create_date"): bindparam("create_date"),
                                                                                                                             self.get_column_name("create_by"): bindparam("create_by"),
                                                                                                                             self.get_column_name("last_modif_date"): bindparam("last_modif_date"),
                                                                                                                             self.get_column_name("last_modif_by"): bindparam("last_modif_by"),
                                                                                                                             self.get_column_name("delete_date"): bindparam("delete_date"),
                                                                                                                             self.get_column_name("delete_by"): bindparam("delete_by"),
                                                                                                                             self.get_column_name("is_readable"): bindparam("is_readable"),
                                                                                                                             self.get_column_name("is_writeable"): bindparam("is_writeable"),
                                                                                                                             self.get_column_name("is_executable"): bindparam("is_executable"),
                                                                                                                             self.get_column_name("posix_permission"): bindparam("posix_permission")
                                                                                                                            })
            async with self._engine.begin() as conn:
                await conn.execute(stmt, [{
                                           "_id": self.get_uuid_from_model(file.id),
                                           "name": file.name,
                                           "path_id": self.get_uuid_from_model(file.path_id),
                                           "extension_id": file.extension_id,
                                           "format_id": file.format_id,
                                           "create_date": file.create_date,
                                           "create_by": file.create_by,
                                           "last_modif_date": file.last_modif_date,
                                           "last_modif_by": file.last_modif_by,
                                           "delete_date": file.delete_date,
                                           "delete_by": file.delete_by,
                                           "is_readable": file.is_readable,
                                           "is_writeable": file.is_writeable,
                                           "is_executable": file.is_executable,
                                           "posix_permission": file.posix_permission
                                          } for file in files])

    @async_timed
    async def delete(self, files: list[File]) -> None:
        if len(files) > 0:
            ids = [self.get_uuid_from_model(file.id) for file in files]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            async with self._engine.begin() as conn:
                await conn.execute(stmt)


class SnowflakeSQlAlchemyFileAsyncDAO(SQlAlchemyFileAsyncDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(SnowflakeSQlAlchemyFileAsyncDAO, self).__init__()

    @async_timed
    async def upsert(self, files: list[File]) -> None:
        if len(files) > 0:
            temp_table = Table(self.get_table_name("{}file".format(constant.TEMP_TABLE_PREFIX)),
                               self._metadata,
                           Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                               Column(self.get_column_name("name"), String(150), nullable=False),
                               Column(self.get_column_name("path_id"), self.get_uuid_type(), nullable=False),
                               Column(self.get_column_name("extension_id"), Integer, nullable=False),
                               Column(self.get_column_name("format_id"), Integer, nullable=False),
                               Column(self.get_column_name("create_date"), TIMESTAMP(timezone=True), nullable=False),
                               Column(self.get_column_name("create_by"), String(50), nullable=False),
                               Column(self.get_column_name("last_modif_date"), TIMESTAMP(timezone=True), nullable=False),
                               Column(self.get_column_name("last_modif_by"), String(50), nullable=False),
                               Column(self.get_column_name("delete_date"), TIMESTAMP(timezone=True), nullable=True),
                               Column(self.get_column_name("delete_by"), String(50), nullable=True),
                               Column(self.get_column_name("is_readable"), Boolean, nullable=False),
                               Column(self.get_column_name("is_writeable"), Boolean, nullable=False),
                               Column(self.get_column_name("is_executable"), Boolean, nullable=False),
                               Column(self.get_column_name("posix_permission"), String(4), nullable=True),
                               *(self.get_meta_columns()),
                               schema=constant.TEMP_SCHEMA,
                               keep_existing=True)
            temp_table.create(self._engine)
            stmt = insert(temp_table).values([{
                                               self.get_column_name("id"): self.get_uuid_from_model(file.id),
                                               self.get_column_name("name"): file.name,
                                               self.get_column_name("path_id"): self.get_uuid_from_model(file.path_id),
                                               self.get_column_name("extension_id"): file.extension_id,
                                               self.get_column_name("format_id"): file.format_id,
                                               self.get_column_name("create_date"): file.create_date,
                                               self.get_column_name("create_by"): file.create_by,
                                               self.get_column_name("last_modif_date"): file.last_modif_date,
                                               self.get_column_name("last_modif_by"): file.last_modif_by,
                                               self.get_column_name("delete_date"): file.delete_date,
                                               self.get_column_name("delete_by"): file.delete_by,
                                               self.get_column_name("is_readable"): file.is_readable,
                                               self.get_column_name("is_writeable"): file.is_writeable,
                                               self.get_column_name("is_executable"): file.is_executable,
                                               self.get_column_name("posix_permission"): file.posix_permission
                                              } for file in files])
            async with self._engine.begin() as conn:
                await conn.execute(stmt)

            merge = MergeInto(target=self._table,
                              source=temp_table,
                              on=(getattr(self._table.c, self.get_column_name("id")) == getattr(temp_table.c, self.get_column_name("id"))))
            val = {
                   self.get_column_name("name"): getattr(temp_table.c, self.get_column_name("name")),
                   self.get_column_name("path_id"): getattr(temp_table.c, self.get_column_name("path_id")),
                   self.get_column_name("extension_id"): getattr(temp_table.c, self.get_column_name("extension_id")),
                   self.get_column_name("format_id"): getattr(temp_table.c, self.get_column_name("format_id")),
                   self.get_column_name("create_date"): getattr(temp_table.c, self.get_column_name("create_date")),
                   self.get_column_name("create_by"): getattr(temp_table.c, self.get_column_name("create_by")),
                   self.get_column_name("last_modif_date"): getattr(temp_table.c, self.get_column_name("last_modif_date")),
                   self.get_column_name("last_modif_by"): getattr(temp_table.c, self.get_column_name("last_modif_by")),
                   self.get_column_name("delete_date"): getattr(temp_table.c, self.get_column_name("delete_date")),
                   self.get_column_name("delete_by"): getattr(temp_table.c, self.get_column_name("delete_by")),
                   self.get_column_name("is_readable"): getattr(temp_table.c, self.get_column_name("is_readable")),
                   self.get_column_name("is_writeable"): getattr(temp_table.c, self.get_column_name("is_writeable")),
                   self.get_column_name("is_executable"): getattr(temp_table.c, self.get_column_name("is_executable")),
                   self.get_column_name("posix_permission"): getattr(temp_table.c, self.get_column_name("posix_permission"))
                  }
            merge.when_matched_then_update().values(**val)
            val[self.get_column_name("id")] = getattr(temp_table.c, self.get_column_name("id"))
            merge.when_not_matched_then_insert().values(**val)
            async with self._engine.begin() as conn:
                await conn.execute(merge)

            temp_table.drop(self._engine)


class EventLevelDAO(DAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(EventLevelDAO, self).__init__()


class SQlAlchemyEventLevelDAO(EventLevelDAO, SQLAlchemyDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        EventLevelDAO.__init__(self)
        SQLAlchemyDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("event_level"),
                                   self._metadata,
                                   Column(self.get_column_name("code"), String(10), nullable=False),
                                   Column(self.get_column_name("name"), String(100), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("code"), name=self.get_key_name("event_level_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @timed
    def get(self, code: str | None = None) -> EventLevel | dict[str, EventLevel] | None:
        if code is None:
            levels = {}
            stmt = select(self._table)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            for row in res:
                level = EventLevel(getattr(row, self.get_column_name("code")))
                level.name = getattr(row, self.get_column_name("name"))
                levels[level.code] = level
            return levels
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("code")) == code)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            row = res.first()
            level = None
            if level is not None:
                level = EventLevel(getattr(row, self.get_column_name("code")))
                level.name = getattr(row, self.get_column_name("name"))
            return level

    @timed
    def create(self, levels: list[EventLevel]) -> None:
        if len(levels) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("code"): level.code,
                                                self.get_column_name("name"): level.name
                                               } for level in levels])
            with self._engine.begin() as conn:
                conn.execute(stmt)

    @timed
    def update(self, levels: list[EventLevel]) -> None:
        if len(levels) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("code")) == bindparam("code")).values({
                                                                                                                                self.get_column_name("name"): bindparam("name")
                                                                                                                               })
            with self._engine.begin() as conn:
                conn.execute(stmt, [{
                                     "code": level.code,
                                     "name": level.name
                                    } for level in levels])

    @timed
    def delete(self, levels: list[EventLevel]) -> None:
        if len(levels) > 0:
            codes = [level.code for level in levels]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("code")).in_(codes))
            with self._engine.begin() as conn:
                conn.execute(stmt)


class EventLevelAsyncDAO(AsyncDAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(EventLevelAsyncDAO, self).__init__()


class SQlAlchemyEventLevelAsyncDAO(EventLevelAsyncDAO, SQLAlchemyAsyncDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        EventLevelAsyncDAO.__init__(self)
        SQLAlchemyAsyncDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("event_level"),
                                   self._metadata,
                                   Column(self.get_column_name("code"), String(10), nullable=False),
                                   Column(self.get_column_name("name"), String(100), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("code"), name=self.get_key_name("event_level_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @async_timed
    async def get(self, code: str | None = None) -> EventLevel | dict[str, EventLevel] | None:
        if code is None:
            levels = {}
            stmt = select(self._table)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            for row in res:
                level = EventLevel(getattr(row, self.get_column_name("code")))
                level.name = getattr(row, self.get_column_name("name"))
                levels[level.code] = level
            return levels
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("code")) == code)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            row = res.first()
            level = None
            if level is not None:
                level = EventLevel(getattr(row, self.get_column_name("code")))
                level.name = getattr(row, self.get_column_name("name"))
            return level

    @async_timed
    async def create(self, levels: list[EventLevel]) -> None:
        if len(levels) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("code"): level.code,
                                                self.get_column_name("name"): level.name
                                               } for level in levels])
            async with self._engine.begin() as conn:
                await conn.execute(stmt)

    @async_timed
    async def update(self, levels: list[EventLevel]) -> None:
        if len(levels) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("code")) == bindparam("code")).values({
                                                                                                                                self.get_column_name("name"): bindparam("name")
                                                                                                                               })
            async with self._engine.begin() as conn:
                await conn.execute(stmt, [{
                                           "code": level.code,
                                           "name": level.name
                                          } for level in levels])

    @async_timed
    async def delete(self, levels: list[EventLevel]) -> None:
        if len(levels) > 0:
            codes = [level.code for level in levels]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("code")).in_(codes))
            async with self._engine.begin() as conn:
                await conn.execute(stmt)


class EventGroupDAO(DAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(EventGroupDAO, self).__init__()


class SQlAlchemyEventGroupDAO(EventGroupDAO, SQLAlchemyDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        EventGroupDAO.__init__(self)
        SQLAlchemyDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("event_group"),
                                   self._metadata,
                                   Column(self.get_column_name("code"), String(3), nullable=False),
                                   Column(self.get_column_name("name"), String(100), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("code"), name=self.get_key_name("event_group_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @timed
    def get(self, code: str | None = None) -> EventGroup | dict[str, EventGroup] | None:
        if code is None:
            groups = {}
            stmt = select(self._table)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            for row in res:
                group = EventGroup(getattr(row, self.get_column_name("code")))
                group.name = getattr(row, self.get_column_name("name"))
                groups[group.code] = group
            return groups
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("code")) == code)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            row = res.first()
            group = None
            if row is not None:
                group = EventGroup(getattr(row, self.get_column_name("code")))
                group.name = getattr(row, self.get_column_name("name"))
            return group

    @timed
    def create(self, groups: list[EventGroup]) -> None:
        if len(groups) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("code"): group.code,
                                                self.get_column_name("name"): group.name
                                               } for group in groups])
            with self._engine.begin() as conn:
                conn.execute(stmt)

    @timed
    def update(self, groups: list[EventGroup]) -> None:
        if len(groups) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("code")) == bindparam("code")).values({
                                                                                                                                self.get_column_name("name"): bindparam("name")
                                                                                                                               })
            with self._engine.begin() as conn:
                conn.execute(stmt, [{
                                     "code": group.code,
                                     "name": group.name
                                    } for group in groups])

    @timed
    def delete(self, groups: list[EventGroup]) -> None:
        if len(groups) > 0:
            codes = [group.code for group in groups]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("code")).in_(codes))
            with self._engine.begin() as conn:
                conn.execute(stmt)


class EventGroupAsyncDAO(AsyncDAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(EventGroupAsyncDAO, self).__init__()


class SQlAlchemyEventGroupAsyncDAO(EventGroupAsyncDAO, SQLAlchemyAsyncDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        EventGroupAsyncDAO.__init__(self)
        SQLAlchemyAsyncDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("event_group"),
                                   self._metadata,
                                   Column(self.get_column_name("code"), String(3), nullable=False),
                                   Column(self.get_column_name("name"), String(100), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("code"), name=self.get_key_name("event_group_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @async_timed
    async def get(self, code: str | None = None) -> EventGroup | dict[str, EventGroup] | None:
        if code is None:
            groups = {}
            stmt = select(self._table)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            for row in res:
                group = EventGroup(getattr(row, self.get_column_name("code")))
                group.name = getattr(row, self.get_column_name("name"))
                groups[group.code] = group
            return groups
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("code")) == code)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            row = res.first()
            group = None
            if row is not None:
                group = EventGroup(getattr(row, self.get_column_name("code")))
                group.name = getattr(row, self.get_column_name("name"))
            return group

    @async_timed
    async def create(self, groups: list[EventGroup]) -> None:
        if len(groups) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("code"): group.code,
                                                self.get_column_name("name"): group.name
                                               } for group in groups])
            async with self._engine.begin() as conn:
                await conn.execute(stmt)

    @async_timed
    async def update(self, groups: list[EventGroup]) -> None:
        if len(groups) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("code")) == bindparam("code")).values({
                                                                                                                                self.get_column_name("name"): bindparam("name")
                                                                                                                               })
            async with self._engine.begin() as conn:
                await conn.execute(stmt, [{
                                           "code": group.code,
                                           "name": group.name
                                          } for group in groups])

    @async_timed
    async def delete(self, groups: list[EventGroup]) -> None:
        if len(groups) > 0:
            codes = [group.code for group in groups]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("code")).in_(codes))
            async with self._engine.begin() as conn:
                await conn.execute(stmt)


class ActionDAO(DAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(ActionDAO, self).__init__()


class SQlAlchemyActionDAO(ActionDAO, SQLAlchemyDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        ActionDAO.__init__(self)
        SQLAlchemyDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("action"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), Integer, nullable=False),
                                   Column(self.get_column_name("code"), String(10), nullable=False),
                                   Column(self.get_column_name("name"), String(50), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("action_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @timed
    def get(self, id_: int | None = None) -> Action | dict[int, Action] | None:
        if id_ is None:
            actions = {}
            stmt = select(self._table)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            for row in res:
                action = Action(getattr(row, self.get_column_name("id")))
                action.code = getattr(row, self.get_column_name("code"))
                action.name = getattr(row, self.get_column_name("name"))
                actions[action.id] = action
            return actions
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == id_)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            row = res.first()
            action = None
            if row is not None:
                action = Action(getattr(row, self.get_column_name("id")))
                action.code = getattr(row, self.get_column_name("code"))
                action.name = getattr(row, self.get_column_name("name"))
            return action

    @timed
    def create(self, actions: list[Action]) -> None:
        if len(actions) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): action.id,
                                                self.get_column_name("code"): action.code,
                                                self.get_column_name("name"): action.name
                                               } for action in actions])
            with self._engine.begin() as conn:
                conn.execute(stmt)

    @timed
    def update(self, actions: list[Action]) -> None:
        if len(actions) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("code"): bindparam("code"),
                                                                                                                             self.get_column_name("name"): bindparam("name")
                                                                                                                            })
            with self._engine.begin() as conn:
                conn.execute(stmt, [{
                                     "_id": action.id,
                                     "code": action.code,
                                     "name": action.name
                                    } for action in actions])

    @timed
    def delete(self, actions: list[Action]) -> None:
        if len(actions) > 0:
            ids = [action.id for action in actions]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            with self._engine.begin() as conn:
                conn.execute(stmt)


class ActionAsyncDAO(AsyncDAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(ActionAsyncDAO, self).__init__()


class SQlAlchemyActionAsyncDAO(ActionAsyncDAO, SQLAlchemyAsyncDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        ActionAsyncDAO.__init__(self)
        SQLAlchemyAsyncDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("action"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), Integer, nullable=False),
                                   Column(self.get_column_name("code"), String(10), nullable=False),
                                   Column(self.get_column_name("name"), String(50), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("action_pk")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @async_timed
    async def get(self, id_: int | None = None) -> Action | dict[int, Action] | None:
        if id_ is None:
            actions = {}
            stmt = select(self._table)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            for row in res:
                action = Action(getattr(row, self.get_column_name("id")))
                action.code = getattr(row, self.get_column_name("code"))
                action.name = getattr(row, self.get_column_name("name"))
                actions[action.id] = action
            return actions
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == id_)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            row = res.first()
            action = None
            if row is not None:
                action = Action(getattr(row, self.get_column_name("id")))
                action.code = getattr(row, self.get_column_name("code"))
                action.name = getattr(row, self.get_column_name("name"))
            return action

    @async_timed
    async def create(self, actions: list[Action]) -> None:
        if len(actions) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): action.id,
                                                self.get_column_name("code"): action.code,
                                                self.get_column_name("name"): action.name
                                               } for action in actions])
            async with self._engine.begin() as conn:
                await conn.execute(stmt)

    @async_timed
    async def update(self, actions: list[Action]) -> None:
        if len(actions) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("code"): bindparam("code"),
                                                                                                                             self.get_column_name("name"): bindparam("name")
                                                                                                                            })
            async with self._engine.begin() as conn:
                await conn.execute(stmt, [{
                                           "_id": action.id,
                                           "code": action.code,
                                           "name": action.name
                                          } for action in actions])

    @async_timed
    async def delete(self, actions: list[Action]) -> None:
        if len(actions) > 0:
            ids = [action.id for action in actions]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            async with self._engine.begin() as conn:
                await conn.execute(stmt)


class EventDAO(DAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(EventDAO, self).__init__()


class SQlAlchemyEventDAO(EventDAO, SQLAlchemyDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        EventDAO.__init__(self)
        SQLAlchemyDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("event"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                                   Column(self.get_column_name("level_code"), String(10), nullable=False),
                                   Column(self.get_column_name("group_code"), String(3), nullable=False),
                                   Column(self.get_column_name("action_id"), Integer, nullable=True),
                                   Column(self.get_column_name("msg"), String(250), nullable=False),
                                   Column(self.get_column_name("source"), String(80), nullable=True),
                                   Column(self.get_column_name("create_date"), TIMESTAMP(timezone=True), nullable=False),
                                   Column(self.get_column_name("create_by"), String(50), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("event_pk")),
                                   ForeignKeyConstraint([self.get_column_name("level_code")],
                                                        ["{}.{}".format(self.get_table_name("event_level", "file"), self.get_column_name("code"))],
                                                        name=self.get_key_name("event_fk1")),
                                   ForeignKeyConstraint([self.get_column_name("group_code")],
                                                        ["{}.{}".format(self.get_table_name("event_group", "file"), self.get_column_name("id"))],
                                                        name=self.get_key_name("event_fk2")),
                                   ForeignKeyConstraint([self.get_column_name("action_id")],
                                                        ["{}.{}".format(self.get_table_name("action", "file"), self.get_column_name("id"))],
                                                        name=self.get_key_name("event_fk3")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @timed
    def get(self, id_: Id | None = None) -> Event | dict[Id, Event] | None:
        if id_ is None:
            events = {}
            stmt = select(self._table)
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            for row in res:
                event = Event(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                event.level_code = getattr(row, self.get_column_name("level_code"))
                event.group_code = getattr(row, self.get_column_name("group_code"))
                event.action_id = getattr(row, self.get_column_name("action_id"))
                event.msg = getattr(row, self.get_column_name("msg"))
                event.source = getattr(row, self.get_column_name("source"))
                event.create_date = getattr(row, self.get_column_name("create_date"))
                event.create_by = getattr(row, self.get_column_name("create_by"))
                events[event.id] = event
            return events
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == self.get_uuid_from_model(id_))
            with self._engine.begin() as conn:
                res = conn.execute(stmt)
            row = res.first()
            event = None
            if row is not None:
                event = Event(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                event.level_code = getattr(row, self.get_column_name("level_code"))
                event.group_code = getattr(row, self.get_column_name("group_code"))
                event.action_id = getattr(row, self.get_column_name("action_id"))
                event.msg = getattr(row, self.get_column_name("msg"))
                event.source = getattr(row, self.get_column_name("source"))
                event.create_date = getattr(row, self.get_column_name("create_date"))
                event.create_by = getattr(row, self.get_column_name("create_by"))
            return event

    @timed
    def create(self, events: list[Event]) -> None:
        if len(events) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): self.get_uuid_from_model(event.id),
                                                self.get_column_name("level_code"): event.level_code,
                                                self.get_column_name("group_code"): event.group_code,
                                                self.get_column_name("action_id"): event.action_id,
                                                self.get_column_name("msg"): event.msg,
                                                self.get_column_name("source"): event.source,
                                                self.get_column_name("create_date"): event.create_date,
                                                self.get_column_name("create_by"): event.create_by
                                               } for event in events])
            with self._engine.begin() as conn:
                conn.execute(stmt)

    @timed
    def update(self, events: list[Event]) -> None:
        if len(events) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("level_code"): bindparam("level_code"),
                                                                                                                             self.get_column_name("group_code"): bindparam("group_code"),
                                                                                                                             self.get_column_name("action_id"): bindparam("action_id"),
                                                                                                                             self.get_column_name("msg"): bindparam("msg"),
                                                                                                                             self.get_column_name("source"): bindparam("source"),
                                                                                                                             self.get_column_name("create_date"): bindparam("create_date"),
                                                                                                                             self.get_column_name("create_by"): bindparam("create_by")
                                                                                                                            })
            with self._engine.begin() as conn:
                conn.execute(stmt, [{
                                     "_id": self.get_uuid_from_model(event.id),
                                     "level_code": event.level_code,
                                     "group_code": event.group_code,
                                     "action_id": event.action_id,
                                     "msg": event.msg,
                                     "source": event.source,
                                     "create_date": event.create_date,
                                     "create_by": event.create_by
                                    } for event in events])

    @timed
    def delete(self, events: list[Event]) -> None:
        if len(events) > 0:
            ids = [self.get_uuid_from_model(event.id) for event in events]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            with self._engine.begin() as conn:
                conn.execute(stmt)


class SnowflakeSQlAlchemyEventDAO(SQlAlchemyEventDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(SnowflakeSQlAlchemyEventDAO, self).__init__()

    @timed
    def upsert(self, events: list[Event]) -> None:
        if len(events) > 0:
            temp_table = Table(self.get_table_name("{}event".format(constant.TEMP_TABLE_PREFIX)),
                               self._metadata,
                               Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                               Column(self.get_column_name("level_code"), String(10), nullable=False),
                               Column(self.get_column_name("group_code"), String(3), nullable=False),
                               Column(self.get_column_name("action_id"), Integer, nullable=True),
                               Column(self.get_column_name("msg"), String(250), nullable=False),
                               Column(self.get_column_name("source"), String(80), nullable=True),
                               Column(self.get_column_name("create_date"), TIMESTAMP(timezone=True), nullable=False),
                               Column(self.get_column_name("create_by"), String(50), nullable=False),
                               *(self.get_meta_columns()),
                               schema=constant.TEMP_SCHEMA,
                               keep_existing=True)
            temp_table.create(self._engine)
            stmt = insert(temp_table).values([{
                                               self.get_column_name("id"): self.get_uuid_from_model(event.id),
                                               self.get_column_name("level_code"): event.level_code,
                                               self.get_column_name("group_code"): event.group_code,
                                               self.get_column_name("action_id"): event.action_id,
                                               self.get_column_name("msg"): event.msg,
                                               self.get_column_name("source"): event.source,
                                               self.get_column_name("create_date"): event.create_date,
                                               self.get_column_name("create_by"): event.create_by
                                              } for event in events])
            with self._engine.begin() as conn:
                conn.execute(stmt)

            merge = MergeInto(target=self._table,
                              source=temp_table,
                              on=(getattr(self._table.c, self.get_column_name("id")) == getattr(temp_table.c, self.get_column_name("id"))))
            val = {
                   self.get_column_name("level_code"): getattr(temp_table.c, self.get_column_name("level_code")),
                   self.get_column_name("group_code"): getattr(temp_table.c, self.get_column_name("group_code")),
                   self.get_column_name("action_id"): getattr(temp_table.c, self.get_column_name("action_id")),
                   self.get_column_name("msg"): getattr(temp_table.c, self.get_column_name("msg")),
                   self.get_column_name("source"): getattr(temp_table.c, self.get_column_name("source")),
                   self.get_column_name("create_date"): getattr(temp_table.c, self.get_column_name("create_date")),
                   self.get_column_name("create_by"): getattr(temp_table.c, self.get_column_name("create_by"))
                  }
            merge.when_matched_then_update().values(**val)
            val[self.get_column_name("id")] = getattr(temp_table.c, self.get_column_name("id"))
            merge.when_not_matched_then_insert().values(**val)
            with self._engine.begin() as conn:
                conn.execute(merge)

            temp_table.drop(self._engine)


class EventAsyncDAO(AsyncDAO, ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(EventAsyncDAO, self).__init__()


class SQlAlchemyEventAsyncDAO(EventAsyncDAO, SQLAlchemyAsyncDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        EventAsyncDAO.__init__(self)
        SQLAlchemyAsyncDAO.__init__(self)

    def _init_table(self) -> None:
        self._table: Table = Table(self.get_table_name("event"),
                                   self._metadata,
                                   Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                                   Column(self.get_column_name("level_code"), String(10), nullable=False),
                                   Column(self.get_column_name("group_code"), String(3), nullable=False),
                                   Column(self.get_column_name("action_id"), Integer, nullable=True),
                                   Column(self.get_column_name("msg"), String(250), nullable=False),
                                   Column(self.get_column_name("source"), String(80), nullable=True),
                                   Column(self.get_column_name("create_date"), TIMESTAMP(timezone=True), nullable=False),
                                   Column(self.get_column_name("create_by"), String(50), nullable=False),
                                   PrimaryKeyConstraint(self.get_column_name("id"), name=self.get_key_name("event_pk")),
                                   ForeignKeyConstraint([self.get_column_name("level_code")],
                                                        ["{}.{}".format(self.get_table_name("event_level", "file"), self.get_column_name("code"))],
                                                        name=self.get_key_name("event_fk1")),
                                   ForeignKeyConstraint([self.get_column_name("group_code")],
                                                        ["{}.{}".format(self.get_table_name("event_group", "file"), self.get_column_name("id"))],
                                                        name=self.get_key_name("event_fk2")),
                                   ForeignKeyConstraint([self.get_column_name("action_id")],
                                                        ["{}.{}".format(self.get_table_name("action", "file"), self.get_column_name("id"))],
                                                        name=self.get_key_name("event_fk3")),
                                   *(self.get_meta_columns()),
                                   schema=self.get_schema_name(),
                                   keep_existing=True)

    @async_timed
    async def get(self, id_: Id | None = None) -> Event | dict[Id, Event] | None:
        if id_ is None:
            events = {}
            stmt = select(self._table)
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            for row in res:
                event = Event(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                event.level_code = getattr(row, self.get_column_name("level_code"))
                event.group_code = getattr(row, self.get_column_name("group_code"))
                event.action_id = getattr(row, self.get_column_name("action_id"))
                event.msg = getattr(row, self.get_column_name("msg"))
                event.source = getattr(row, self.get_column_name("source"))
                event.create_date = getattr(row, self.get_column_name("create_date"))
                event.create_by = getattr(row, self.get_column_name("create_by"))
                events[event.id] = event
            return events
        else:
            stmt = select(self._table).where(getattr(self._table.c, self.get_column_name("id")) == self.get_uuid_from_model(id_))
            async with self._engine.begin() as conn:
                res = await conn.execute(stmt)
            row = res.first()
            event = None
            if row is not None:
                event = Event(Id(self.get_uuid_from_db(getattr(row, self.get_column_name("id")))))
                event.level_code = getattr(row, self.get_column_name("level_code"))
                event.group_code = getattr(row, self.get_column_name("group_code"))
                event.action_id = getattr(row, self.get_column_name("action_id"))
                event.msg = getattr(row, self.get_column_name("msg"))
                event.source = getattr(row, self.get_column_name("source"))
                event.create_date = getattr(row, self.get_column_name("create_date"))
                event.create_by = getattr(row, self.get_column_name("create_by"))
            return event

    @async_timed
    async def create(self, events: list[Event]) -> None:
        if len(events) > 0:
            stmt = insert(self._table).values([{
                                                self.get_column_name("id"): self.get_uuid_from_model(event.id),
                                                self.get_column_name("level_code"): event.level_code,
                                                self.get_column_name("group_code"): event.group_code,
                                                self.get_column_name("action_id"): event.action_id,
                                                self.get_column_name("msg"): event.msg,
                                                self.get_column_name("source"): event.source,
                                                self.get_column_name("create_date"): event.create_date,
                                                self.get_column_name("create_by"): event.create_by
                                               } for event in events])
            async with self._engine.begin() as conn:
                await conn.execute(stmt)

    @async_timed
    async def update(self, events: list[Event]) -> None:
        if len(events) > 0:
            stmt = update(self._table).where(getattr(self._table.c, self.get_column_name("id")) == bindparam("_id")).values({
                                                                                                                             self.get_column_name("level_code"): bindparam("level_code"),
                                                                                                                             self.get_column_name("group_code"): bindparam("group_code"),
                                                                                                                             self.get_column_name("action_id"): bindparam("action_id"),
                                                                                                                             self.get_column_name("msg"): bindparam("msg"),
                                                                                                                             self.get_column_name("source"): bindparam("source"),
                                                                                                                             self.get_column_name("create_date"): bindparam("create_date"),
                                                                                                                             self.get_column_name("create_by"): bindparam("create_by")
                                                                                                                            })
            async with self._engine.begin() as conn:
                await conn.execute(stmt, [{
                                           "_id": self.get_uuid_from_model(event.id),
                                           "level_code": event.level_code,
                                           "group_code": event.group_code,
                                           "action_id": event.action_id,
                                           "msg": event.msg,
                                           "source": event.source,
                                           "create_date": event.create_date,
                                           "create_by": event.create_by
                                          } for event in events])

    @async_timed
    async def delete(self, events: list[Event]) -> None:
        if len(events) > 0:
            ids = [self.get_uuid_from_model(event.id) for event in events]
            stmt = delete(self._table).where(getattr(self._table.c, self.get_column_name("id")).in_(ids))
            async with self._engine.begin() as conn:
                await conn.execute(stmt)


class SnowflakeSQlAlchemyEventAsyncDAO(SQlAlchemyEventAsyncDAO):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(SnowflakeSQlAlchemyEventAsyncDAO, self).__init__()

    @async_timed
    async def upsert(self, events: list[Event]) -> None:
        if len(events) > 0:
            temp_table = Table(self.get_table_name("{}event".format(constant.TEMP_TABLE_PREFIX)),
                               self._metadata,
                               Column(self.get_column_name("id"), self.get_uuid_type(), nullable=False),
                               Column(self.get_column_name("level_code"), String(10), nullable=False),
                               Column(self.get_column_name("group_code"), String(3), nullable=False),
                               Column(self.get_column_name("action_id"), Integer, nullable=True),
                               Column(self.get_column_name("msg"), String(250), nullable=False),
                               Column(self.get_column_name("source"), String(80), nullable=True),
                               Column(self.get_column_name("create_date"), TIMESTAMP(timezone=True), nullable=False),
                               Column(self.get_column_name("create_by"), String(50), nullable=False),
                               *(self.get_meta_columns()),
                               schema=constant.TEMP_SCHEMA,
                               keep_existing=True)
            temp_table.create(self._engine)
            stmt = insert(temp_table).values([{
                                               self.get_column_name("id"): self.get_uuid_from_model(event.id),
                                               self.get_column_name("level_code"): event.level_code,
                                               self.get_column_name("group_code"): event.group_code,
                                               self.get_column_name("action_id"): event.action_id,
                                               self.get_column_name("msg"): event.msg,
                                               self.get_column_name("source"): event.source,
                                               self.get_column_name("create_date"): event.create_date,
                                               self.get_column_name("create_by"): event.create_by
                                              } for event in events])
            async with self._engine.begin() as conn:
                await conn.execute(stmt)

            merge = MergeInto(target=self._table,
                              source=temp_table,
                              on=(getattr(self._table.c, self.get_column_name("id")) == getattr(temp_table.c, self.get_column_name("id"))))
            val = {
                   self.get_column_name("level_code"): getattr(temp_table.c, self.get_column_name("level_code")),
                   self.get_column_name("group_code"): getattr(temp_table.c, self.get_column_name("group_code")),
                   self.get_column_name("action_id"): getattr(temp_table.c, self.get_column_name("action_id")),
                   self.get_column_name("msg"): getattr(temp_table.c, self.get_column_name("msg")),
                   self.get_column_name("source"): getattr(temp_table.c, self.get_column_name("source")),
                   self.get_column_name("create_date"): getattr(temp_table.c, self.get_column_name("create_date")),
                   self.get_column_name("create_by"): getattr(temp_table.c, self.get_column_name("create_by"))
                  }
            merge.when_matched_then_update().values(**val)
            val[self.get_column_name("id")] = getattr(temp_table.c, self.get_column_name("id"))
            merge.when_not_matched_then_insert().values(**val)
            async with self._engine.begin() as conn:
                await conn.execute(merge)

            temp_table.drop(self._engine)


class FileDBModel(ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(FileDBModel, self).__init__()

    @abstractmethod
    def update_locations(self, changes: dict[str, list]) -> None:
        raise NotImplementedError("Should implement update_locations()")

    @abstractmethod
    def update_files(self, changes: dict[str, list]) -> None:
        raise NotImplementedError("Should implement update_files()")

    @abstractmethod
    def update_events(self, changes: dict[str, list]) -> None:
        raise NotImplementedError("Should implement update_events()")


class SQLAlchemyFileDBModel(FileDBModel, SQLAlchemyDBModel):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        FileDBModel.__init__(self)
        SQLAlchemyDBModel.__init__(self)

    def update_locations(self, changes: dict[str, list]) -> None:
        self.daos["location"].create(changes[constant.DB_OPE_CREATE])
        self.log.logger.debug("{} locations have been created into database".format(len(changes[constant.DB_OPE_CREATE])))

        self.daos["location"].update(changes[constant.DB_OPE_UPDATE])
        self.log.logger.debug("{} locations have been created into database".format(len(changes[constant.DB_OPE_UPDATE])))

        self.daos["location"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} locations have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))

    def update_files(self, changes: dict[str, list]) -> None:
        self.daos["file"].create(changes[constant.DB_OPE_CREATE])
        self.log.logger.debug("{} files have been created into database".format(len(changes[constant.DB_OPE_CREATE])))

        self.daos["file"].update(changes[constant.DB_OPE_UPDATE])
        self.log.logger.debug("{} files have been updated into database".format(len(changes[constant.DB_OPE_UPDATE])))

        self.daos["file"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} files have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))

    def update_events(self, changes: dict[str, list]) -> None:
        self.daos["event"].create(changes[constant.DB_OPE_CREATE])
        self.log.logger.debug("{} events have been created into database".format(len(changes[constant.DB_OPE_CREATE])))

        self.daos["event"].update(changes[constant.DB_OPE_UPDATE])
        self.log.logger.debug("{} events have been updated into database".format(len(changes[constant.DB_OPE_UPDATE])))

        self.daos["event"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} events have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))


class SnowflakeSQLAlchemyFileDBModel(SQLAlchemyFileDBModel):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(SnowflakeSQLAlchemyFileDBModel, self).__init__()

    def update_locations(self, changes: dict[str, list]) -> None:
        create_update_changes = changes[constant.DB_OPE_CREATE] + changes[constant.DB_OPE_UPDATE]
        self.daos["location"].upsert(create_update_changes)
        self.log.logger.debug("{} locations have been created or updated into database".format(len(create_update_changes)))

        self.daos["location"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} locations have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))

    def update_files(self, changes: dict[str, list]) -> None:
        create_update_changes = changes[constant.DB_OPE_CREATE] + changes[constant.DB_OPE_UPDATE]
        self.daos["file"].upsert(create_update_changes)
        self.log.logger.debug("{} files have been created or updated into database".format(len(create_update_changes)))

        self.daos["file"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} files have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))

    def update_events(self, changes: dict[str, list]) -> None:
        create_update_changes = changes[constant.DB_OPE_CREATE] + changes[constant.DB_OPE_UPDATE]
        self.daos["event"].upsert(create_update_changes)
        self.log.logger.debug("{} events have been created or updated into database".format(len(create_update_changes)))

        self.daos["event"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} events have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))


class FileAsyncDBModel(ABC):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(FileAsyncDBModel, self).__init__()

    @abstractmethod
    async def update_locations(self, changes: dict[str, list]) -> None:
        raise NotImplementedError("Should implement update_locations()")

    @abstractmethod
    async def update_files(self, changes: dict[str, list]) -> None:
        raise NotImplementedError("Should implement update_files()")

    @abstractmethod
    async def update_events(self, changes: dict[str, list]) -> None:
        raise NotImplementedError("Should implement update_events()")


class SQLAlchemyFileAsyncDBModel(FileAsyncDBModel, SQLAlchemyAsyncDBModel):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        FileAsyncDBModel.__init__(self)
        SQLAlchemyAsyncDBModel.__init__(self)

    async def update_locations(self, changes: dict[str, list]) -> None:
        await self.daos["location"].create(changes[constant.DB_OPE_CREATE])
        self.log.logger.debug("{} locations have been created into database".format(len(changes[constant.DB_OPE_CREATE])))

        await self.daos["location"].update(changes[constant.DB_OPE_UPDATE])
        self.log.logger.debug("{} locations have been created into database".format(len(changes[constant.DB_OPE_UPDATE])))

        await self.daos["location"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} locations have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))

    async def update_files(self, changes: dict[str, list]) -> None:
        await self.daos["file"].create(changes[constant.DB_OPE_CREATE])
        self.log.logger.debug("{} files have been created into database".format(len(changes[constant.DB_OPE_CREATE])))

        await self.daos["file"].update(changes[constant.DB_OPE_UPDATE])
        self.log.logger.debug("{} files have been updated into database".format(len(changes[constant.DB_OPE_UPDATE])))

        await self.daos["file"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} files have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))

    async def update_events(self, changes: dict[str, list]) -> None:
        await self.daos["event"].create(changes[constant.DB_OPE_CREATE])
        self.log.logger.debug("{} events have been created into database".format(len(changes[constant.DB_OPE_CREATE])))

        await self.daos["event"].update(changes[constant.DB_OPE_UPDATE])
        self.log.logger.debug("{} events have been updated into database".format(len(changes[constant.DB_OPE_UPDATE])))

        await self.daos["event"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} events have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))


class SnowflakeSQLAlchemyFileAsyncDBModel(SQLAlchemyFileAsyncDBModel):
    """
    classdocs
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super(SnowflakeSQLAlchemyFileAsyncDBModel, self).__init__()

    async def update_locations(self, changes: dict[str, list]) -> None:
        create_update_changes = changes[constant.DB_OPE_CREATE] + changes[constant.DB_OPE_UPDATE]
        await self.daos["location"].upsert(create_update_changes)
        self.log.logger.debug("{} locations have been created or updated into database".format(len(create_update_changes)))

        await self.daos["location"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} locations have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))

    async def update_files(self, changes: dict[str, list]) -> None:
        create_update_changes = changes[constant.DB_OPE_CREATE] + changes[constant.DB_OPE_UPDATE]
        await self.daos["file"].upsert(create_update_changes)
        self.log.logger.debug("{} files have been created or updated into database".format(len(create_update_changes)))

        await self.daos["file"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} files have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))

    async def update_events(self, changes: dict[str, list]) -> None:
        create_update_changes = changes[constant.DB_OPE_CREATE] + changes[constant.DB_OPE_UPDATE]
        await self.daos["event"].upsert(create_update_changes)
        self.log.logger.debug("{} events have been created or updated into database".format(len(create_update_changes)))

        await self.daos["event"].delete(changes[constant.DB_OPE_DELETE])
        self.log.logger.debug("{} events have been removed from database".format(len(changes[constant.DB_OPE_DELETE])))
