#include "Libraria.h"

#include <stdio.h>
#include <iostream>
#include <iomanip>

Library::Library()//Конструктор бібліотеки
{
    currentDate = 0;//День створеня
    holdings.reserve(100);//вмістимість книг
    members.reserve(100);//вмістимість користувачів
}

/******************************************************************************
* Вхід: Пустота
*
* Вихід: отримання інофрмацію про книгу і додавання її у відповідний вектор
*
* Мета: додавання книги в бібліотеку
******************************************************************************/
void Library::addBook()
{
    std::string idCode, title, author; // інформація про книгу

    std::cout << "What is the book's ID code?" << std::endl;
    //Зчитування id книги
    getline(std::cin, idCode);

    //перевірка чи Id не повторюється
    for (int i = 0; i < holdings.size(); i++)
    {
        if (holdings[i].getIdCode() == idCode)
        {
            std::cout << "That ID is already in use." << std::endl;
            return;
        }
    }

    std::cout << "\nWhat is the title of the book?" << std::endl;
    getline(std::cin, title);
    std::cout << "\nWho is the author of the book?" << std::endl;
    getline(std::cin, author);
    //Оголошення нової книги і додавання її у відповідний вектор
    Book newBook(idCode, title, author);
    holdings.push_back(newBook);
}

/******************************************************************************
* Вхід: Пустота
*
* Вихід: Отримання інформації про нового користувача і додавання
*       його у відповідний вектор
*
* Мета: додавання користувача в бібліотеку
******************************************************************************/
void Library::addMember()
{
    std::string idCode, name; // інформація про користувача

    std::cout << "What is the member's ID code?" << std::endl;
    //Зчитування id користувача
    getline(std::cin, idCode);

    //перевірка ID на унікальність
    for (int i = 0; i < members.size(); i++)
    {
        if (members[i].getIdNum() == idCode)
        {
            std::cout << "That ID is already in use." << std::endl;
            return;
        }
    }

    std::cout << "\nWhat is the member's name?" << std::endl;
    getline(std::cin, name);
    //Оголошення нового користувача і додавання його у відповідний вектор
    Patron newMem(idCode, name);
    members.push_back(newMem);
}


/******************************************************************************
* Вхід:  Тут використовуємо дві строки, одна це парметри користувача,
*         що хоче взяти книгу і друга , це параметри книги, що хочуть взяти
*
* Вихід: Перевіряє чи книгу може бути взята користувачем і якщо так
*        то змінити положення книги і добавити її цьому кристувачеві
*        в список взятих книг
*
* Мета: Взятя книги з бібліотеки
******************************************************************************/
void Library::checkOutBook(std::string patronID, std::string bookID)
{
    Patron* member = memberCheck(patronID); // вказівник на користувача з відповідним ID
                        // Пустота якщо неіснує
    Book* book = bookCheck(bookID); // вказівник на книжку з відповідним ID
                    // Пустота якщо неіснує
    //Перевірка чи користувач може взяти книгу
    //Перевірка чи користувач існує
    if (member == NULL)
    {
        std::cout << "\nThat is an invalid member ID." << std::endl;
    }//Перевірка чи книга існує
    else if (book == NULL)
    {
        std::cout << "\nThat book is not a part of this library." << std::endl;
    }//Перевірка чи ми вже не взяли цю книгу
    else if (book->getLocation() == 2)
    {
        std::cout << "\nThat book is already checked out." << std::endl;
    }//Перевірка чи її не взяв хтось інший
    else if (book->getLocation() == 1
        && book->getRequestedBy()->getIdNum() != member->getIdNum())
    {
        std::cout << "\nThat book is on hold by another member." << std::endl;
    }//Якщо проблеми не виявлено
    else
    {
        //Встановлення відповідних параметрів
        book->setCheckedOutBy(member);//назва користувача, що взяв книгу
        book->setDateCheckedOut(currentDate);//відповідна дата
        book->setLocation(CHECKED_OUT);//зміна положення книги, на *на руках*
        if (book->getLocation() == 1)//якщо книга взята
            book->setRequestedBy(NULL);//зміна параметру запросів на пустоту
        member->addBook(book);//додавання книги користувачу
        std::cout << "\n" << book->getTitle() << " has been checked out by "
            << member->getName() << "." << std::endl;
    }
}

/******************************************************************************
* Вхід: Тільки один параметр, що вказує на id код книжки
*
* Вихід: Перевіряє чи книгу може бути повернута користувачем і якщо так
*        то змінити положення книги і видалити її цьому кристувачеві
*        з списку взятих книг
*
* Мета: Поверння книги в бібліотеку
******************************************************************************/
void Library::returnBook(std::string bookID)
{
    Book* book = bookCheck(bookID); // вказівник на книгу з відповідним ID
    // Пустота якщо книга не існує
    if (book == NULL)
    {
        std::cout << "\nThat book is not a part of this library." << std::endl;
    }//Якщо книгу не брали
    else if (book->getLocation() != 2)
    {
        std::cout << "\nThat book is not checked out." << std::endl;
    }
    else
    {//вказівник на персону, що брала книгу і виклик функції повернення книги
        Patron* member = book->getCheckedOutBy();
        member->removeBook(book);//

        if (book->getRequestedBy() != NULL)//Якщо книгу хтось запросив, 
            book->setLocation(ON_HOLD);   //то зміна положення *на руках*
        else
            book->setLocation(ON_SHELF);//в іншому випадку в бібліотеці

        book->setCheckedOutBy(NULL);//Значення книги взята користувачем тепер відсутнє
        std::cout << "\n" << book->getTitle() << " has been returned." << std::endl;
    }
}


/******************************************************************************
* Вхід:  Тут використовуємо дві строки, одна це парметри користувача,
*         що хоче взяти книгу і друга , це параметри книги, що хочуть взяти
*
* Вихід: Перевіряє чи книга може бути взята користувачем і якщо так
*        то змінити положення книги на список бажання користувача(requestedBy)
*
* Мета: Запит на повернення книги в зону очікування
******************************************************************************/
void Library::requestBook(std::string patronID, std::string bookID)
{
    Patron* member = memberCheck(patronID); // вказівник на користувача з відповідним ID
                        // Пустота якщо неіснує
    Book* book = bookCheck(bookID); // вказівник на книгу з відповідним ID
    // Пустота якщо користувач не існує
    if (member == NULL)
    {
        std::cout << "\nThat is not a valid member ID." << std::endl;
    }//Пустота ,якщо книги не існує
    else if (book == NULL)
    {
        std::cout << "\nThat book is not a part of this library." << std::endl;
    }//Якщо книга кимось взята
    else if (book->getRequestedBy() != NULL)
    {
        std::cout << "\nThat book is on hold by another member." << std::endl;
    }
    else
    {//Якщо хтось залишив запит на книгу
        book->setRequestedBy(member);
        if (book->getLocation() == 0)// Зміна початкового положення книги
            book->setLocation(ON_HOLD);// на положення на руках
        std::cout << "\n" << book->getTitle() << " has been requested by "
            << member->getName() << "." << std::endl;
    }
}

/******************************************************************************
* Вхід: Пустота
*
* Вихід: Збільшує кількість днів від якого бібліотека була створена і додає
*        до заборгованоїплати(fineAmount) кожного користувача, по просрочив
*     тримання книги в себе
*
* Мета: зміна дати і перерахунок за боргованої плати за потреби
******************************************************************************/
void Library::incrementCurrentDate()
{
    currentDate++;//Збільшення показника дня
    for (int i = 0; i < holdings.size(); i++)//Для кожного пройденого дня
    {
        if (holdings[i].getLocation() == 2 &&//Для тих хто має книгу *на руках*
            ((currentDate - holdings[i].getDateCheckedOut()) > Book::CHECK_OUT_LENGTH))//І У НИХ ВИЙшов час тримання книги в себе
        {
            holdings[i].getCheckedOutBy()->amendFine(DAILY_FINE);//Збільшити параметр заборгованості
        }
    }
    std::cout << "The date is now " << currentDate << "." << std::endl;
}

/******************************************************************************
* Вхід: Два параметри, один це строка з id користувача, який хоче заплатити
*       заборгованість, і один double в якому вказуємо суму платежу
*
* Вихід: Зменшує заюоргованість користувача в меншу сторону
*
* Мета: Випалата заборгованості
******************************************************************************/
void Library::payFine(std::string patronID, double payment)
{
    Patron* member = memberCheck(patronID); // вказівник на користувача з відповідним ID
    // Пустота якщо користувача не існує
    if (member == NULL)
    {
        std::cout << "\nThat is an invalid member ID" << std::endl;
    }
    else
    {//Оголошення платні
        member->amendFine(0 - payment);
        std::cout << "\nThe fines for " << member->getName()//заборгованість для користувача
            << " are now $" << std::fixed << std::showpoint << std::setprecision(2)//складає+Допоміжні команди+
            << member->getFineAmount() << "." << std::endl;//+виправлена заборгованість
    }
}


/******************************************************************************
* Вхід: Один парамерт з парметром іd користувача
*
* Вихід: вивід інформації про користувача з відповідним йому id
*
* Мета: Вивід інформації про користувача
******************************************************************************/
void Library::viewPatronInfo(std::string patronID)
{
    Patron* member = memberCheck(patronID); // вказівник на користувача з відповідним ID
                        // Пустота якщо неіснує
    std::string line;
    //зміна використовується для друку лінії
    line.assign(20, '-');
    //
    if (member == NULL)
    {
        std::cout << "\nThe is an invalid member ID" << std::endl;
    }
    else
    {
        std::cout << std::left << std::setw(16) << "\nID NUMBER:" << member->getIdNum()//Виведення іd користувача
            << "\n" << std::endl;
        std::cout << std::setw(15) << "NAME:" << member->getName() << std::endl;//Виведення імені користувача
        std::cout << std::setw(15) << "\nCHECKED OUT BOOKS:" << std::endl;//Книг, що він взяв
        std::cout << line << std::endl;
        for (int i = 0; i < member->getCheckedOutBooks().size(); i++)//Для кожної взятої книги
        {
            std::cout << std::setw(20) << member->getCheckedOutBooks()[i]->getTitle()//назву книги
                << std::endl;
            std::cout << line << std::endl;
        }
        std::cout << "\nCURRENT FINES: $" << std::fixed << std::showpoint << std::setprecision(2)//заборгованість користувача
            << member->getFineAmount() << std::endl;
    }
}

/******************************************************************************
* Вхід: Один парамерт з парметром іd книги
*
* Вихід: вивід інформації про книгу з відповідною їй id
*
* Мета: Вивід інформації про книгу
******************************************************************************/
void Library::viewBookInfo(std::string bookID)
{
    Book* book = bookCheck(bookID); // вказівник на книгу з відповідним ID
    // Пустота якщо неіснує
    if (book == NULL)
    {
        std::cout << "\nThat book is not a part of this library" << std::endl;
    }
    else
    {//Виведення інформації про книгу
        std::cout << std::left << std::setw(21) << "\nID CODE:" << book->getIdCode()
            << "\n" << std::endl;
        std::cout << std::setw(20) << "TITLE:" << book->getTitle() << "\n" << std::endl;
        std::cout << std::setw(20) << "AUTHOR" << book->getAuthor() << "\n" << std::endl;
        std::cout << std::setw(20) << "LOCATION";
        //Інформація про її положення
        if (book->getLocation() == 0)
        {
            std::cout << "On the shelf\n" << std::endl;
        }
        else if (book->getLocation() == 1)
        {
            std::cout << "On hold\n" << std::endl;
        }
        else
        {
            std::cout << "Checked out\n" << std::endl;
            std::cout << std::setw(20) << "CHECKED OUT BY:" << book->getCheckedOutBy()->getName()//Імя того хто взяв
                << "\n" << std::endl;
            std::cout << std::setw(20) << "DUE DATE:"
                << (book->getDateCheckedOut() + book->CHECK_OUT_LENGTH) << "\n"//Кількість днів книги *на руках*
                << std::endl;
        }
        if (book->getRequestedBy() != NULL)//Якщо хтось робив запит
        {
            std::cout << std::setw(20) << "REQUESTED BY:" << book->getRequestedBy()->getName()//Показати хто його робив
                << std::endl;
        }
    }
}


