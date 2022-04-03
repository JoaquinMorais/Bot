import random


class Preguntados:
    def __init__(self):
        self.preguntas = ['¿Cuántas zonas horarias tiene en Rusia?',
        '¿Cuántas franjas tiene la bandera de Estados Unidos?',
        '¿Cuál es el animal nacional de Australia?',
        'En un Año viciesto, ¿Cuántos días le toma a la tierra dar una vuelta a la órbita del sol?',
        '¿Cuál de los siguientes imperios no tenía un idioma escrito?',
        '¿Cómo se llamaba Istanbul antes de 1923?',
        '¿Qué país tiene la mayor cantidad de islas en el mundo? (Mas de 220.000!!!)',
        '¿Cual es el pais mas pequeño del mundo?',
        '¿Cuál es la capital de Canadá?',
        'Cual es la cordillera más larga (no más alta) del mundo?',
        '¿Dónde se encuentra la fosa más profunda del océano?',
        '¿Cuál es el río más largo del mundo?',
        '¿Cuál es la serie de libros mejor vendida del siglo 21?',
        '¿Cuál es el idioma que tiene más palabras (según su diccionario)?',
        '¿Cuál es la obra más famosa de Edvard Munch?',
        '¿Qué artista pinto el techo de la Capilla Sixtina en Roma?',
        '¿Cuándo se inauguró el metro de Londres?',
        '¿Cual fue el primer pais de America en lograr su independencia?',
        '¿De dónde es Billie Eilish?',
        '¿De qué ciudad son originarios los Beatles?',
        '¿Cuál es la canción más reproducida en Spotify hasta el momento?',
        '¿Cuántas teclas tiene un piano?',
        '¿Qué banda americana se llamaba originalmente, “Kara’s Flowers”?',
        '¿Qué equipo de fútbol se le conoce como ‘The Red Devils’?',
        '¿Qué conductor de la Formula 1 ha ganado más campeonatos?',
        '¿Originalmente cómo se llamaba la marca Nike?',
        '¿En qué año se fundó Netflix?',
        '¿Cuál fue la serie más vista en Netflix en el 2019?',
        '¿Cómo se llama la icónica cafetería de Friends?',
        '¿Cuál fue la primer película de Disney?',
        '¿Cual es la primera película de la saga de “El Hobbit”?',
        '¿Cual es la capital de Austria?',
        '¿De qué país se independizó Eslovenia?',
        '¿Qué país africano fue fundado por esclavos americanos liberados en 1847?'
        ]
        self.respuestas = [
        ['11','12','9','10'],
        ['13','10','15','18'],
        ['El Canguro','El Koala','El Wombat','El Cocodrilo Poroso'],
        ['366','365','364','367'],
        ['Inca','Aztecas','Griego','Egipcio'],
        ['Constantinopla','Benjin','Marchisal','Aragon'],
        ['Suecia','Japon','Indonesia','Nueva Zelanda'],
        ['El Vaticano','Monaco','San Marino','Andorra'],
        ['Ottawa','Vancouver','Toronto','Montreal'],
        ['Los Andes','Cordillera de Alaska ','Los Alpes','Sierra Madre'],
        ['Fosa De Las Marinas','Fosa de Kermadec','Fosa de las Kuriles','Fosa de Filipinas'],
        ['Amazonas ','Nilo','Yangtsé','Misisipi'],
        ['Harry Potter','El Señor De Los Anillos','El Principito','Crepusculo'],
        ['Ingles','Español','Chino','Portugues'],
        ['El Grito','La Gioconda (La Mona Lisa)','La Noche Estrellada','El Nacimiento De Venus'],
        ['Miguel Angel','Diego Velazquez','Leonardo Da Vinci','Pablo Picasso'],
        ['1863','1845','1893','1874'],
        ['Haiti','Estados Unidos','Mexico','Colombia'],
        ['Los Angeles','New York','Misisipi','Miami'],
        ['Liverpool','Manchester','Nevada','Seattle'],
        ['The Shape of You','Believer','Despacito','Marolio'],
        ['88','92','96','102'],
        ['Maroon 5','The Rolling Stones','The Beatles','ACBC'],
        ['Manchester United','Madrid','Sevilla','Valencia'],
        ['Michael Schumacher','Jackie Stewart','Ayrton Senna','Didier Pironi'],
        ['Blue Ribbon Sports','Tnks','Strakers','Nykaas'],
        ['1997','2001','2009','2005'],
        ['Stranger Things','The Office','The Walking Dead','The Simpsons'],
        ['Central Perk','Little Collins','Frisson Espresso','Brooklyn Roasting Company'],
        ['Blanca Nieves','Cenicienta','Babylon','Dumbo'],
        ['Un Viaje Inesperado','La Desolacion De Smaug','La Batalla De Los Cinco Ejercitos','La Comunidad Del Anillo'],
        ['Viena','Varsovia','Berlin','Budapest'],
        ['Yugoslavia','Del Imperio Austriaco','Croacia','Italia'],
        ['Liberia','Ghana','Sokoto','Benin']
        ]


    def Jugar(self):
        n = random.randint(0, len(self.preguntas)-1)
        print(n)
        return self.preguntas[n], self.respuestas[n]
    def Contar(self):
        print(len(self.preguntas))
        print(len(self.respuestas))



