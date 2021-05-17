export AUTH0_DOMAIN = 'alessandromalhotra.eu.auth0.com'
export ALGORITHMS = ["RS256"]
export API_AUDIENCE = 'https://localhost:5001'
export DB_HOST = '127.0.0.1:5432'
export DB_USER = 'postgres'
export DB_PASSWORD = 'password123'
export DB_NAME = 'capstone_test'
export DB_PATH = 'postgresql://{}:{}@{}/{}'.format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
export CASTING_ASSISTANT_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1qQXBDWVhYUThwM3lWNVJJTWRCSyJ9.eyJpc3MiOiJodHRwczovL2FsZXNzYW5kcm9tYWxob3RyYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5YmE1MGNhN2FlNTgwMDZlYTdmYTU1IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NTAwMSIsImlhdCI6MTYyMTI3MDkxMywiZXhwIjoxNjIxMjc4MTEzLCJhenAiOiJacnNhcXZiR2l0ZVdja0ZDYlY1OVZZc04yR0l4UERlTiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzL2luZGl2aWR1YWwiXX0.j0617muOiYHiXYoJZKOfSL0d5Hm_SST_acIL7aOFAc4-2SZAOcSrYCFzMl6svfk1KvIBHoCnOf9pIBC9Rek9jYmhRf7fHx-L2-ESV0SpahI4mF_1SCOOtc50dmqOexk6tSas9YnjS9KYvIzxWXnjgz5az_Vc7J3nq5_MSgmcOBTjxMLP-iroTJ0aaOZVIpYnOMm_ZvM6k5c_wm3QzVkVhMegyG1M2w7mV9NCOfP-eoqsxGcX7O4a7Uwzzi2Y7LWED1AAIORyd4eRMYH8PXznfYsOj3PHySLwtI4FfrUsxUmxLKtI7eDkFffJGkDQmVH5QYR5bUfcHsllvNryOvnJlw'
export CASTING_DIRECTOR_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1qQXBDWVhYUThwM3lWNVJJTWRCSyJ9.eyJpc3MiOiJodHRwczovL2FsZXNzYW5kcm9tYWxob3RyYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA2MWIzYzc2MDFkOGMwMDZlYmRmNDc5IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NTAwMSIsImlhdCI6MTYyMTI3MTIzMCwiZXhwIjoxNjIxMjc4NDMwLCJhenAiOiJacnNhcXZiR2l0ZVdja0ZDYlY1OVZZc04yR0l4UERlTiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycy9kZWxldGUiLCJkZWxldGU6bW92aWVzL2RlbGV0ZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy9pbmRpdmlkdWFsIiwicG9zdDphY3RvcnMvY3JlYXRlIiwicG9zdDptb3ZpZXMvY3JlYXRlIl19.MAzgTUc-TLYDu9Usuad7lpD_0Vfu1-i1ouVdq0nY6jZEkfr8cStgc7ly4u4FAK7jo5iliXL8MpnDwUKvhxBFYC1rZSpGnRgDs5IsqHZ0QLtfQJmrVAAIVBz3aNzdjeJgQ1PQ3FrFFjte5Ee_dAGoL-m_Vt065UcoFVd493LqpRxVnNNcUKXyiyeHp5mjtfGM7NGxscWfu9TbK9DPfN46noZcy3PZ3TkWQjRk8dwr19jjyhBMY4D7mfsF0iwBImsiB-4DUzg5LfelKJD4t_YhoVaL9YBsib5tAyOq8nwgouEabBQrrAKd8ig09ZOCOiPpqSRsaQ05P-SAT'
export EXECUTIVE_PRODUCER_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1qQXBDWVhYUThwM3lWNVJJTWRCSyJ9.eyJpc3MiOiJodHRwczovL2FsZXNzYW5kcm9tYWxob3RyYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA1NDg0NzdlNTUyNjYwMDY4ZDY3ZDIyIiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NTAwMSIsImlhdCI6MTYyMTI3MTM0NywiZXhwIjoxNjIxMjc4NTQ3LCJhenAiOiJacnNhcXZiR2l0ZVdja0ZDYlY1OVZZc04yR0l4UERlTiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycy9kZWxldGUiLCJkZWxldGU6bW92aWVzL2RlbGV0ZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy9pbmRpdmlkdWFsIiwicGF0Y2g6YWN0b3JzL3VwZGF0ZSIsInBhdGNoOm1vdmllcy91cGRhdGUiLCJwb3N0OmFjdG9ycy9jcmVhdGUiLCJwb3N0Om1vdmllcy9jcmVhdGUiXX0.dbR8WVXN1HXzxuC11TMmUOIFvCsBkVWLfq4KVBGi2psFKtwAsXyJ1o0KKF98Vu9ZRe7xogc5E8g0MyGR6ianc9fMjKcB_kM_m4RQ0A5eSZo94cloCAT7KsS1HvFyCfjDRh2fgBztn-aWsrjfq6BxvWKlGA54r0PQOY1HwmgsLXbuiNK956JqXHWyehe0eeAtx4WR_EU9z5abIa5piZJ1ZJnLnKXaaK1ms7iaATM3MqUYNWHyWr62SIKKQprpQ1SUpWhApsECaTecxinUHfKJy7A7c0u4p2B3LWN8JJ7YFj6buVCjnAFI9JL9BCh8m7E1Klv7-eFSH1Erp_m14Ov_pA'