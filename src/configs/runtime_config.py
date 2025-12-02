from archipy.configs.base_config import BaseConfig


class RuntimeConfig(BaseConfig):
    def customize(self) -> None:
        self.FASTAPI.PROJECT_NAME = "FastAPI-Archipy Boilerplate"
        self.FASTAPI.DOCS_URL = "/docs"

        # This is only for this boilerplate, don`t use in production environment
        #TODO remove for production
        import os
        import tempfile

        temp_dir = tempfile.gettempdir()
        db_file = os.path.join(temp_dir, "test_db.sqlite")
        self.SQLITE_SQLALCHEMY.DRIVER_NAME = "sqlite+aiosqlite"
        self.SQLITE_SQLALCHEMY.DATABASE = db_file



BaseConfig.set_global(RuntimeConfig())
