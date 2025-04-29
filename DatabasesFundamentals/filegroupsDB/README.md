1. Filegroups e Arquivos de Dados
 Os filegroups são grupos de arquivos de dados (.mdf e .ndf) que permitem organizar o
armazenamento das tabelas e índices em diferentes locais físicos. Isso pode melhorar o
desempenho e facilitar o gerenciamento do banco de dados.
● Filegroup Primário (PRIMARY):
 Função: Armazena metadados do banco de dados e tabelas que não foram atribuídas outros
filegroups.
 Arquivo: universidade.mdf
 Tamanho Inicial: 5120 KB
 Crescimento: 1024 KB
 Critério: O filegroup primário é obrigatório e geralmente usado para armazenar informações
essenciais do banco de dados.
● Filegroup fg_cursos:
 Função: Armazena a tabela Curso.
 Arquivo: cursos.ndf
 Tamanho Inicial: 1024 KB
 Crescimento: 10%
 Critério: A tabela Curso é pequena e não cresce rapidamente, por isso foi alocada em um
filegroup separado com crescimento moderado.
● Filegroup fg_alunos:
 Função: Armazena a tabela Aluno.
 Arquivo: alunos.ndf
 Tamanho Inicial: 2048 KB
 Crescimento: 15%
 Critério: A tabela Aluno pode crescer rapidamente devido ao grande número de alunos, por
isso foi alocada em um filegroup com maior tamanho inicial e crescimento percentual.
● Filegroup fg_professores:
 Função: Armazena a tabela Professor.
 Arquivo: professores.ndf
 Tamanho Inicial: 1024 KB
 Crescimento: 10%
 Critério: A tabela Professor é pequena e estável, com crescimento lento, por isso foi alocada
em um filegroup com crescimento moderado.
● Filegroup fg_disciplinas:
 Função: Armazena a tabela Disciplina.
 Arquivo: disciplinas.ndf
 Tamanho Inicial: 2048 KB
 Crescimento: 15%
 Critério: A tabela Disciplina pode crescer conforme novas disciplinas são adicionadas, por
isso foi alocada em um filegroup com crescimento percentual.
● Filegroup fg_turmas:
 Função: Armazena as tabelas Turma e Aluno_Turma.
 Arquivo: turmas.ndf
 Tamanho Inicial: 3072 KB
 Crescimento: 20%
 Critério: As tabelas Turma e Aluno_Turma podem crescer rapidamente devido ao grande
número de turmas e matrículas, por isso foram alocadas em um filegroup com maior tamanho
inicial e crescimento percentual.
● Arquivo de Log (LOG ON):
 Função: Armazena o log de transações do banco de dados.
 Arquivo: universidade_log.ldf
 Tamanho Inicial: 1024 KB
 Crescimento: 10%
 Critério: O arquivo de log é essencial para garantir a integridade dos dados e permitir a
recuperação em caso de falhas. O crescimento percentual é usado para evitar fragmentação.
2. Organização das Tabelas nos Filegroups
 Cada tabela foi associada a um filegroup específico com base no seguinte critério:
● Tabela Curso: Armazenada no filegroup fg_cursos.
 Critério: Tabela pequena e estável, com crescimento lento.
● Tabela Aluno: Armazenada no filegroup fg_alunos.
 Critério: Tabela que pode crescer rapidamente devido ao grande número de alunos.
● Tabela Professor: Armazenada no filegroup fg_professores.
 Critério: Tabela pequena e estável, com crescimento lento.
● Tabela Disciplina: Armazenada no filegroup fg_disciplinas.
 Critério: Tabela que pode crescer conforme novas disciplinas são adicionadas.
● Tabela Turma: Armazenada no filegroup fg_turmas.
 Critério: Tabela que pode crescer rapidamente devido ao grande número de turmas.
● Tabela Aluno_Turma: Armazenada no filegroup fg_turmas.
 Critério: Tabela de relacionamento que pode crescer rapidamente devido ao grande número
de matrículas.
3. Vantagens da Organização por Filegroups
● Desempenho: Distribuir as tabelas em diferentes filegroups permite que operações de leitura
e escrita sejam realizadas em paralelo, melhorando o desempenho.
● Gerenciamento: Facilita o backup e a recuperação de partes específicas do banco de dados.
● Escalabilidade: Permite adicionar novos arquivos de dados ou filegroups conforme o banco de
dados cresce.