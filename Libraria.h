#pragma once
#ifndef LIBRARIA_H
#define LIBRARIA_H

#include <string>
#include<vector>
#include "Book.h"
#include "Patron.h"


//Клас_3 Бібліотека
class Library
{
private:
    std::vector<Book> holdings; //вектор книг в бібліотеці
    std::vector<Patron> members; //вектор користувачів в бібліотеці
    int currentDate; //День з якого відкрилась бібліотека
    Patron* memberCheck(std::string patronID);//Вказівник на id користувача
    Book* bookCheck(std::string bookID);//Вказівник на id книги

public:
    double DAILY_FINE = 0.1;//платня за день
    Library();
    void addBook();
    void addMember();
    void checkOutBook(std::string patronID, std::string bookID);
    void returnBook(std::string bookID);
    void requestBook(std::string patronID, std::string bookID);
    void incrementCurrentDate();
    void payFine(std::string patronID, double payment);
    void viewPatronInfo(std::string patronID);
    void viewBookInfo(std::string bookID);
};

#endif // !LIBRARY_H
