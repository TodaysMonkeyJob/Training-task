#pragma once
#ifndef BOOK_H
#define BOOK_H

#include "Patron.h"
#include <string>
#include <vector>

//Позиція книги
enum Locale { ON_SHELF, ON_HOLD, CHECKED_OUT };

class Patron;

//Клас_1 Книга
class Book
{
private:
    std::string idCode; //Унікальний ідентифікатор
    std::string title; //Назва книжки
    std::string author; //Автор книжки
    Locale location; //Де знаходиться книжка
    Patron* checkedOutBy; //Людина, яка зараз має книгу
    Patron* requestedBy; //Людина, яка хоче книгу
    int dateCheckedOut; //Кількість часу, яку книгу тримає у себе читач
public:
    static const int CHECK_OUT_LENGTH = 14; //Кількість днів, що дозволено для залишання в себе
    //конструктор книги
    Book();
    Book(std::string idc, std::string t, std::string a);

    std::string getIdCode() //отримання id_Коду
    {
        return idCode;
    }

    std::string getTitle() //отримання назви
    {
        return title;
    }

    std::string getAuthor() //отримання автора
    {
        return author;
    }

    Locale getLocation() //отримання місцеположення книги
    {
        return location;
    }

    void setLocation(Locale lo) //встановлення місцеположення книги
    {
        location = lo;
    }

    Patron* getCheckedOutBy() //повернення вказуівника на персону, що взяла книгу
    {
        return checkedOutBy;
    }

    void setCheckedOutBy(Patron* p) //встановити, що видана на руки тому то
    {
        checkedOutBy = p;
    }

    Patron* getRequestedBy() //повернення вказуівника на персону, що  запросила книгу
    {
        return requestedBy;
    }

    void setRequestedBy(Patron* p) //встановити, що запрошує на руки той то
    {
        requestedBy = p;
    }

    int getDateCheckedOut() //повернути таймер днів від видачі
    {
        return dateCheckedOut;
    }

    void setDateCheckedOut(int d) //встановитити таймер днів від видачі
    {
        dateCheckedOut = d;
    }
};

#endif // !BOOK_H


