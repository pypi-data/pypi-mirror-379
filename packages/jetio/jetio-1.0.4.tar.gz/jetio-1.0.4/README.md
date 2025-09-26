# Jetio
![Jetio Logo](https://github.com/cehstephen/jetio/raw/main/jetio_main_logo.png)
### The Zero-Boilerplate Python Framework for Rapid API Development

![PyPI Version](https://img.shields.io/pypi/v/jetio?style=for-the-badge)

**Jetio** is a modern, high-performance Python web framework designed to transform your SQLAlchemy models directly into fully-featured, production-ready REST APIs with minimal code. Stop writing boilerplate and start building what matters.

---

## Key Features

* **Model-Driven APIs:** Use standard SQLAlchemy models as your single source of truth for your database, validation, and API serialization.
* **Automatic CRUD:** Instantly generate robust Create, Read, Update, and Delete endpoints for any model with a single line of code.
* **Secure by Design:** Easily secure your auto-generated endpoints with a single flag and plug in your own authentication logic.
* **Async First:** Built from the ground up on an async core (powered by Starlette) for maximum performance and scalability.
* **Automatic Docs:** Get interactive Swagger UI and ReDoc API documentation out of the box.
* **Flexible & Familiar:** Escape the generator whenever you need to. Use familiar decorator-based routing for custom endpoints, giving you the best of both worlds.

---

- **Visit Jetio Framework** [You can deliver more than 500 times faster with Jetio - see how it works.](https://jetio.org)
- **Jetio Framework oneBenchmark Results:** [We compared Jetio speed with Flask & FastAPI](https://jetio.org/jetio_benchmark_report.html) See the result for yourself.
---

## Example
```python
# model.py
from sqlalchemy.orm import Mapped
from jetio import JetioModel

class User(JetioModel):
    username: Mapped[str]
    email: Mapped[str]

class Minister(JetioModel):
    first_name: Mapped[str]
    last_name: Mapped[str]
```

### Get Jetio to make your app
```python
# app.py
from jetio import Jetio, CrudRouter, add_swagger_ui
from model import User, Minister

app = Jetio()
add_swagger_ui(app)

# Generate 5 CRUD routes per model
CrudRouter(model=User).register_routes(app)
CrudRouter(model=Minister).register_routes(app)


if __name__ == "__main__":
    app.run()
```

## Database setup 
Use your preferred DB tool.

_or for quick dev environment, you can also change your app.py above to:_
```python
# app.py
from jetio import Jetio, CrudRouter, add_swagger_ui, Base, engine
from model import User, Minister
import asyncio

app = Jetio()
add_swagger_ui(app)

# Generate 5 CRUD routes per model
CrudRouter(model=User).register_routes(app)
CrudRouter(model=Minister).register_routes(app)


# --- Database and Server Startup ---
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created.")

if __name__ == "__main__":
    asyncio.run(create_db_and_tables())
    app.run()
```
