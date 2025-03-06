Для виконання даного тестового завдання я проаналізував інформацію про аномальні транзакції та як їх вираховувати, 
а саме за якою формулою, щоб краще розуміти і коректно виконати поставлене завдання.

В першу чергу зі списку транзакцій я виділив лише потрібні поля для підрахунку, а саме "user_id" та "amount". 
Далі з отриманими даними я створив новий список, в якому групуються транзакції по одному користувачу. 
Наступним кроком за формулою проводжу певні підрахунки, щоб знайти стандартне відхилення і порівняти його з [нормою відхилення 2,5](https://uk.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B5_%D0%B2%D1%96%D0%B4%D1%85%D0%B8%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F)
Після підрахунку відхилення воно порівнюється з нормою, і якщо відхилення транзакції більше, то ця транзакція додається до списку аномальних.

Також на свій розсуд я вирішив додати запис списку аномальних транзакцій до JSON файлу для зручності.

Увесь функціонал був зроблений в межах однієї функції. Також була ідея розбити увесь функціонал на окремі функції,
але в процесі написання зрозумів, що в цьому немає сенсу і це є непрактичним.
