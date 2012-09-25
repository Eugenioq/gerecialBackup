gerecialBackup
==============

Script muito simples em Python para realizar backup do aplicativo de frente de Loja Gerencial

	Realiza a compressão da pasta "DADOS" criando um arquivo com a extensão .zip
	Nomeia o arquivo de backup como "backup_gerencial.AAAA-MM-DD.zip"
	Você pode utlizar ainda o Dropbox, Skydrive ou GoogleDrive com esse script e assim salvar o backup na nuvem.  

Esse script deve ser executado no momento que e máquina for desligada. Para que possa ler arquivo "DADAOS.FBD".

Você pode automatizar a execução desse script realizando os seguintes passos:

	Salve o script na seguinte pasta:

	C:\Windows\System32\GroupPolicy\Machine\Scripts\Shutdown

	Esta pasta é somente criada após acessar o as configurações no gpedit.msc

	Vá em Iniciar, Executar e digite: gpedit.msc e navegue até:

	Configurações do computador > Configurações do Windows > Scripts (Inicialização/Encerramento) > Desligar. 
	e selecione o script.

Requerimentos:

	Python 2.7