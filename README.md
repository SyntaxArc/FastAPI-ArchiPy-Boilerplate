# FastAPI-ArchiPy-Boilerplate

A simple FastAPI boilerplate using ArchiPy's clean architecture principles.

## Overview

This project implements a clean architecture approach with FastAPI, providing a structured and maintainable codebase. It leverages ArchiPy to organize code into distinct layers with clear separation of concerns.

## Features

- Clean Architecture implementation via ArchiPy
- FastAPI for high-performance API development
- Dependency injection with dependency-injector
- SQLAlchemy ORM with async support
- Layered architecture (controllers, logics, repositories)
- Comprehensive linting and type checking

## Prerequisites

- Python 3.13+
- Poetry (for dependency management)
- Make (optional, for using Makefile commands)

## Up and Running

1. **Setup the environment**

   ```bash
   # Install prerequisites
   make setup

   # Install project dependencies
   make install
   # Or for development dependencies:
   make install-dev
   ```

2. **Configure your environment**

   Create environment configuration as needed. The project uses RuntimeConfig for configuration management.

3. **Run the application**

   ```bash
   # Start the application
   python manage.py
   ```

   The API will be available at http://localhost:8000 by default.

4. **API Documentation**

   Once running, access the interactive API documentation at:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Project Structure

```
src/
├── configs/         # Configuration management
├── controllers/     # API endpoints and request handling
├── logics/          # Business logic layer
├── models/          # Data models and schemas
│   ├── dtos/        # Data Transfer Objects
│   ├── entities/    # Domain entities
│   └── types/       # Type definitions
├── repositories/    # Data access layer with adapters
└── utils/           # Utility functions
```

## Development

```bash
# Format code
make format

# Run linters
make lint

# Run behavioral tests
make behave

# Run pre-commit hooks
make pre-commit

# Clean build artifacts
make clean
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the UnLicense - see the [LICENSE](LICENSE) file for details.
