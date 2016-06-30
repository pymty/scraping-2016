# ¿Cómo correr este proyecto?

	# Scrapy no sobreescribe el archivo así que hay que borrarlo
	rm items.json
	scrapy crawl pcel -O items.json

# Modo interactivo
	scrapy shell 'https://www.example.com'

# Iniciar un nuevo spider
	scrapy genspider <nombre> <dominio>

# Reto
	- Crear un spider llamado `sismos` con el dominio `www.ssn.unam.mx`
	- Obtener los sismos recientes