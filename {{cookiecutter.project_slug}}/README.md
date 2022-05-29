### {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}


<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![Checked with mypy](https://camo.githubusercontent.com/59eab954a267c6e9ff1d80e8055de43a0ad771f5e1f3779aef99d111f20bee40/687474703a2f2f7777772e6d7970792d6c616e672e6f72672f7374617469632f6d7970795f62616467652e737667)](http://mypy-lang.org/)
## 💻 DEVELOPMENT

### 🚀 Project running
After cloning the project, you can run it with the following steps (required [docker][docker]):
 1. Create .env file:
    ```shell
    cp .env.template .env
    ```
 2. Set values in .env file.
 3. Run development server:
    ```shell
    docker compose -f docker-compose.dev.yaml up
    ```
    or
    ```shell
    docker-compose -f docker-compose.dev.yaml up
    ```

### 📦 Deployment:
This manual describes the delivery of an application using [docker][docker]. You can deliver the application using [docker-compose][docker-compose], even abandon [docker][docker] and put everything on the server or use other methods and tools, but this will not be described, and you will have to do this at one's own risk.

 1. Install and configure [docker][docker]: [instruction](https://docs.docker.com/engine/install/ubuntu/)

 2. Build [image](https://docs.docker.com/glossary/#image) from [dockerfile](https://docs.docker.com/glossary/#dockerfile):
    ```shell
    docker build . --build-arg SSH_PRIVATE_KEY=<SSH_PRIVATE_KEY> --tag {{ cookiecutter.project_slug }}
    ```
    _`SSH_PRIVATE_KEY` - [ssh][ssh] private [key](https://www.ssh.com/academy/ssh/key), which is used to access the [git][git] [repositories](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) where the source code of the custom private libraries is stored_
    
    _`{{ cookiecutter.project_slug }}` - name of the [image](https://docs.docker.com/glossary/#image) [tag](https://docs.docker.com/engine/reference/commandline/build/#tag-an-image--t). Can be replaced with a custom value_

 3. Run [container](https://docs.docker.com/glossary/#container):
    ```shell
    docker run \
      --env SECRET_KEY=<DJANGO_SECRET_KEY> \
      --env DATABASE_URL=<DATABASE_URL> \
      --env SENTRY_DSN=<SENTRY_DSN> \
      --env DJANGO_STATIC_ROOT=<DJANGO_STATIC_ROOT> \
      --env ALLOWED_HOSTS=<ALLOWED_HOSTS> \
      --name {{ cookiecutter.project_slug }}-backend \
      {{ cookiecutter.project_slug }}
    ```
    where instead of `<...>` specify the corresponding values. For more information on environment variables, see the section on [environment variables](#environment-variables).

    _`{{ cookiecutter.project_slug }}-backend` - [container](https://docs.docker.com/glossary/#container) [name](https://docs.docker.com/engine/reference/run/#name---name). Can be replaced with custom value_

    _`{{ cookiecutter.project_slug }}` - name of the [image](https://docs.docker.com/glossary/#image) [tag](https://docs.docker.com/engine/reference/commandline/build/#tag-an-image--t). Specified in step 2_
    

## 🔖 Environment variables
| Name               | Required           | Default value     | Description                                                                                |
|--------------------|--------------------|-------------------|--------------------------------------------------------------------------------------------|
| DEBUG              | :heavy_minus_sign: | `False`           | A boolean that turns on/off [debug mode][1] in django                                      |
| SECRET_KEY         | :heavy_plus_sign:  | N/A               | [Secret key][2] for django-project                                                         |
| DATABASE_URL       | :heavy_plus_sign:  | N/A               | Link to connect to the database. Link to connect to the database. [This format][4] is used |
| DJANGO_STATIC_ROOT | :heavy_minus_sign: | <BASE_DIR>/static | Directory for storing [static files][4]                                                    |
| SENTRY_DSN         | :heavy_minus_sign: | `None`            | [Sentry DSN][5]                                                                            |
| ALLOWED_HOSTS      | :heavy_plus_sign:  | `[]`              | Django [ALLOWED_HOSTS](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts)  |

[1]: https://docs.djangoproject.com/en/3.2/ref/settings/#debug
[2]: https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key
[4]: https://django-environ.readthedocs.io/en/latest/#environ.environ.Env.db_url
[4]: https://docs.djangoproject.com/en/3.2/ref/settings/#static-root
[5]: https://docs.sentry.io/product/sentry-basics/dsn-explainer/


[pyenv]: https://github.com/pyenv/pyenv
[pyenv-virtualenv]: https://github.com/pyenv/pyenv-virtualenv
[python]: https://python.org
[poetry]: https://python-poetry.org
[postgres]: https://www.postgresql.org
[virtualenv]: https://packaging.python.org/key_projects/#virtualenv
[docker]: https://www.docker.com
[docker-compose]: https://docs.docker.com/compose/
[ssh]: https://www.openssh.com
[git]: https://git-scm.com
