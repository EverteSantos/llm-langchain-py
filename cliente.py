from langserve import RemoteRunnable

chain_remote = RemoteRunnable("http://localhost:8000/tradutor")
texto = chain_remote.invoke({"language": "inglês", "texto": "Importação via API"})
print(texto)