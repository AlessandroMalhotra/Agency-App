export AUTH0_DOMAIN = 'alessandromalhotra.eu.auth0.com'
export ALGORITHMS = ["RS256"]
export API_AUDIENCE = 'https://localhost:5001'
export DB_HOST = '127.0.0.1'
export DB_USER = 'postgres'
export DB_PORT = 5432
export DB_PASSWORD = 'password123'
export DB_NAME = 'capstone'
export DB_PATH = 'postgresql://{}:{}@:{}/{}'.format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
export DATABASE_URL = 'postgres://bicdjymvcuzimg:7295df480fe590a3aba366a6fedbe2c0bafdc94bf9c2b663ef18ef17f06f6e01@ec2-34-233-0-64.compute-1.amazonaws.com:5432/d2po3gvvsf0ao8'
export CASTING_ASSISTANT_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1qQXBDWVhYUThwM3lWNVJJTWRCSyJ9.eyJpc3MiOiJodHRwczovL2FsZXNzYW5kcm9tYWxob3RyYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5YmE1MGNhN2FlNTgwMDZlYTdmYTU1IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NTAwMSIsImlhdCI6MTYyMTM0NzU2NywiZXhwIjoxNjIxNDMzOTY3LCJhenAiOiJacnNhcXZiR2l0ZVdja0ZDYlY1OVZZc04yR0l4UERlTiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzL2luZGl2aWR1YWwiXX0.iqNKBtdxJ_4nBlHB_wu51pK3Ap61YLGLWS9X3IDfLkkjZeHeNRgqCp4l-Ut1dS4NUOTlFynYszX8sj5zUeCsuHcmNUHmMq4QYtsD64jLjrSnK3ZK7GIqgjotKZZXUsGosmk0HzSziscKsmSUIYzhi-SFPNTU_YgCW0QEWaTHjijIgaq90WWWDtuR94_uCdgFmrOPcPGSgfyQ9Xlh4rQbq8TmuDYRfGwP7tQp2LrzpVhpJsqkKFVrs-57nIsQJR7opwaCHZN-MIdahzWmt0aLq6_uyTBdHkNn479OiqbxdBUf2Mkua9Rs9rqVup9fmTJ9I3UD-nShERmGC8N2DYEEWA'
export CASTING_DIRECTOR_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1qQXBDWVhYUThwM3lWNVJJTWRCSyJ9.eyJpc3MiOiJodHRwczovL2FsZXNzYW5kcm9tYWxob3RyYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA2MWIzYzc2MDFkOGMwMDZlYmRmNDc5IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NTAwMSIsImlhdCI6MTYyMTM0NzY4NywiZXhwIjoxNjIxNDM0MDg3LCJhenAiOiJacnNhcXZiR2l0ZVdja0ZDYlY1OVZZc04yR0l4UERlTiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycy9kZWxldGUiLCJkZWxldGU6bW92aWVzL2RlbGV0ZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy9pbmRpdmlkdWFsIiwicG9zdDphY3RvcnMvY3JlYXRlIiwicG9zdDptb3ZpZXMvY3JlYXRlIl19.Iz4ty80jtneZcCcpCV9ZDJscep1lCMUHo2TSQvOsk01S2Sr-BqeuHjE_iW6LpqL0UFxEiqGxCINeZknCyi41NFC9GqJpYuVln62-sjNUHc8_LcmiJ3i8XCXMCoYcibfXkCm27AiZI73flA92eXcaxtWk5brbuh3RWj6r0cPqqVeR-Wuqub3iJyGYKQ97dOdmhg5xvMwWoqBZUwPBYJw1y9VI07A8GYmPNdWGYyHRcdpNowoAt1felwuM0mbeKiCjTp2BSAEawiVTAQFO-q88cwFotbN4QcJG_UwK0GhO1RIXUGXwTSnkLkseRX06LLeEqQ_sOsUgbYvJ51tWFF7jXg'
export EXECUTIVE_PRODUCER_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1qQXBDWVhYUThwM3lWNVJJTWRCSyJ9.eyJpc3MiOiJodHRwczovL2FsZXNzYW5kcm9tYWxob3RyYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA1NDg0NzdlNTUyNjYwMDY4ZDY3ZDIyIiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NTAwMSIsImlhdCI6MTYyMTM0Nzc1OSwiZXhwIjoxNjIxNDM0MTU5LCJhenAiOiJacnNhcXZiR2l0ZVdja0ZDYlY1OVZZc04yR0l4UERlTiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycy9kZWxldGUiLCJkZWxldGU6bW92aWVzL2RlbGV0ZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy9pbmRpdmlkdWFsIiwicGF0Y2g6YWN0b3JzL3VwZGF0ZSIsInBhdGNoOm1vdmllcy91cGRhdGUiLCJwb3N0OmFjdG9ycy9jcmVhdGUiLCJwb3N0Om1vdmllcy9jcmVhdGUiXX0.khZYyMOzcy5D8X5FG7X2C503oMg6Bhk9ODO9TVQiE2pseHJnDfhhRyYj4dBcvBY8uwcmcb1IF8uAh4ryDkn6X8b34PlzP4oCRUwCMRQBzzbH9MNjlgdZjWAPKzqnGqnL4LkufyC6BjMJigAWcezTG9yoEv6kqglJhLfdQVmhmhLdXA6IvIVLMTuZl9iBwvnOmBqQMwFUXe1kpxTNnavLPQvna5twLbldlfW2V6fIURfm-5WPEhxLa9Jg8qP64WnZiyuRhYyi78iHqfyoUADMmG8q1Hw3ljaFS24RFkGrvQ07C7E2M2kGlod44Qw43JFZW63QgMTpVrZz3Wv0jnyTUw'