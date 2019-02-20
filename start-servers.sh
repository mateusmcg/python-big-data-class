# Mudar o nome do arquivo .py que você quer rodar o servidor.

echo "Iniciando servidor: $1"

echo "Criando pasta 'results' para armazenar os resultados"
mkdir results

echo "Aguardando consumidores..."
exec "C:\Python27\python.exe" $1
echo "Execução finalizada"