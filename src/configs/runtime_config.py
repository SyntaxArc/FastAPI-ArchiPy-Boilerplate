from archipy.configs.base_config import BaseConfig


class RuntimeConfig(BaseConfig):
    def customize(self) -> None:
        self.FASTAPI.PROJECT_NAME = "FastAPI-Archipy Boilerplate"
        self.FASTAPI.DOCS_URL = "/docs"

        # This is only for this boilerplate, don`t use in production environment
        import os
        import tempfile

        temp_dir = tempfile.gettempdir()
        db_file = os.path.join(temp_dir, "test_db.sqlite")
        self.SQLALCHEMY.DRIVER_NAME = "sqlite+aiosqlite"
        self.SQLALCHEMY.DATABASE = db_file
        self.SQLALCHEMY.ISOLATION_LEVEL = None
        self.SQLALCHEMY.PORT = None


BaseConfig.set_global(RuntimeConfig())
