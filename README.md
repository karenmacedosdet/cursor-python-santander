# cursor-python-santander
Cursor com Python: desenvolvimento inteligente com IA

**PROJETO 1: Contador de palavras em arquivos de texto**  
- Peça ao usuário o caminho para um arquivo de texto
- Leia o conteúdo do arquivo
- Separe em palavras
- Conte o número total de palavras
- Exibe as 10 palavras mais frequentes e sua contagem


**PROJETO 2: Calculadora simples**

**1. Crie um programa calculator.py que:**
- Solicita ao usuário uma operação (adição, subtração, multiplicação, divisão) e dois números
- Execute a operação e exiba o resultado
- Isso deve ser repetido até que o usuário digite "saída" como uma operação

**2. Use o Cursor para:**
- Sugerir como estruturar o loop principal
- Gerar a lógica para cada operação (talvez usando um dicionário de funções ou if/elif)
- Testar diferentes entradas


**PROJETO 3: FizzBuzz**
- Se o número for um múltiplo de 3, imprima "Fizz"; se for 5, imprima "Buzz"; se ambos, "FizzBuzz"; caso contrário, o número.
- Faça isso no Cursor: Tente escrever apenas o esqueleto do loop for i in range(1, 51): e deixe a IA sugerir o resto. O Cursor provavelmente conhece esse problema popular e completará automaticamente grande parte dele para você.
- Verifique se a saída está correta. Se houver um erro (por exemplo, a IA pode estar errada em algum detalhe), corrija-o manualmente ou diga à IA "Corrija o código de acordo com as regras especificadas."


**PROJETO 4: Análise básica de dados**
- Obtenha um pequeno conjunto de dados, por exemplo, um CSV com duas colunas de números (você pode criá-lo manualmente).
- Escreva um script parse.py que leia o CSV (use o pandas se quiser, o Cursor o ajudará a importá-lo e usá-lo).
- Calcule estatísticas simples: média, mediana, desvio padrão para cada coluna.
- Gere um gráfico de dispersão de uma coluna em relação à outra (aqui você terá que usar o matplotlib; tente perguntar ao Cursor "Trace um gráfico de dispersão de col1 vs. col2").
- Veja como a IA pode até mesmo escrever código Matplotlib para você.
- Execute o script; se estiver no Cursor, o gráfico deverá ser aberto em uma janela externa (ou no painel de plotagem do VS Code, se ativado).
- Este exercício mistura programação com um toque de ciência de dados, demonstrando a versatilidade do Cursor.


**PROJETO 5: Aplicação Web com Flask – “Gerenciador de Tarefas Pessoal”**  
Desenvolver um pequeno aplicativo da Web para gerenciar a lista de tarefas. Os usuários poderão adicionar tarefas, marcá-las como concluídas e ver a lista atual. Usaremos o Flask, uma microestrutura da Web Python muito popular e fácil de aprender. Este projeto abrangerá conceitos de desenvolvimento da Web, como rotas, modelos HTML, formulários e implementação local.

**TESTE COMPLETO DO APLICATIVO:**
- Acesse http://127.0.0.1:5000:
- Você deverá ver o "Gestor de tarefas" e uma lista (vazia no início) e o formulário
- Adicione uma tarefa "Comprar leite" e pressione add (adicionar). Ele deve retornar para / e exibir "Comprar leite [Completar]"
- Pressione [Completar], você deve riscar a opção "Comprar leite"
- Adicione várias tarefas, verifique se as tarefas não concluídas não estão riscadas na parte superior, etc
- Se algo der errado (erro 500 no Flask), verifique o console onde o aplicativo está sendo executado para ver o rastreamento e corrigí-lo


**PROJETO 6: Análise de dados – “Relatório de vendas mensais”**  
Com o objetivo de aprender tarefas comuns de análise de dados, analisar arquivo CSV com dados de vendas de uma loja, com colunas como "data", "produto", "quantidade vendida" e "preço" para obter:  
- Total de vendas por mês
- Produto mais vendido (em quantidade) e produto com a maior receita
- Visualizações: gráfico de vendas por mês, gráfico de vendas por produto (5 principais)
- Gerar um relatório de texto/HTML com esses resultados
- Usar o pandas para a manipulação de dados e o matplotlib para a criação de gráficos


**PROJETO 7: Automatização – “Organizador de Arquivos”**
Criar um script para organizar os arquivos em uma pasta, distribuindo-os em subpastas de acordo com a categoria da sua extensão. Por exemplo, na pasta "Downloads", temos uma mistura de imagens, documentos PDF, vídeos etc. Queremos que o script crie subdiretórios como Imagens, Documentos, Vídeos, Outros e mova cada arquivo para o diretório correspondente de acordo com sua extensão. Esse script pode ser executado manualmente ou programado para ser executado de tempos em tempos, de acordo com as seguintes etapas:
- Defina categorias de extensões: Imagens = [".png", ".jpg", ".jpeg", ".gif"], Documentos = [".pdf", ".docx", ".txt"], Videos = [".mp4", ".avi", ".mkv"], Musica = [".mp3", ".wav"], Outra = [outras extensões]
- Listar todos os arquivos na pasta de destino
- Para cada arquivo, determine sua extensão e, portanto, sua categoria
- Crie a pasta de categoria se ela não existir
- Mova o arquivo para essa pasta
