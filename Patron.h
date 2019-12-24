#pragma once
#ifndef PATRON_H
#define PATRON_H

#include "Book.h"
#include <string>
#include <vector>

class Book;
//Клас_2 Користувач
class Patron
{
private:
    std::string idNum; //Унікальний ідентифікатор
    std::string name; //Імя користувача
    std::vector<Book*> checkedOutBooks; //Книжка, яку користувач взяв на руки
    double fineAmount; //Платня бібліотеці за тримання книг в себе

public:
    Patron() //Стандартний конструктор
    {
        fineAmount = 0;
    }

    Patron(std::string idn, std::string n) //Ініціалізуємо зміну користувач
    {
        idNum = idn, name = n, fineAmount = 0;
    }

    std::string getIdNum() //повертаємо значення IdКоду
    {
        return idNum;
    }

    std::string getName() //повертаємо значення імені
    {
        return name;
    }

    std::vector<Book*> getCheckedOutBooks() //повертаємо значення книг, що взяті користувачем 
    {
        return checkedOutBooks;
    }

    void addBook(Book* b) //додавання книг, до списку взятих користувчем
    {
        checkedOutBooks.push_back(b);
    }

    void removeBook(Book* b);

    double getFineAmount() //повертаємо значення платні за книги
    {
        return fineAmount;
    }

    void amendFine(double amount) //Збільшення платні,якщо перетримав книгу
    {
        fineAmount += amount;
    }
};

#endif // !PATRON_H
