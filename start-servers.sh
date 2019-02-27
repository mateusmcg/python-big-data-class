# Mudar o nome do arquivo .py que você quer rodar o servidor.

echo "Iniciando servidor: exerc23.py"

echo "Criando pasta 'results' para armazenar os resultados"
mkdir results

echo "Aguardando consumidores..."
exec "C:\Python27\python.exe" exerc23.py
echo "Execução finalizada"