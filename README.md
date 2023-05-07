# Twitter API FastAPI

Twitter API REST creada usando FastAPI.
Todos los datos de usuarios y de tweets son guardados en 2 archivos JSON uno para cada uno de estos.

## Endpoints

### Tweets

- home('/')
    - Lista todos los tweets.
- post('/post')
    - Registra un tweet con la información propocionada por un request body.
- show_a_tweet('/tweets/{tweet_id}')
    - Muestra la información de un tweet por su id.

### Users

- signup('/signup')
    - Registra un usuario con la información proporcionada por un request body.
- show_all_users('/users')
    - Lista todos los usuarios.
- show_a_tweet('/users/{tweet_id}')
    - Muestra la información de un tweet por su id.
