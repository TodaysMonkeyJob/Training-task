
#include <stdio.h>
#include <iostream>
#include <iomanip>
#include "Book.h"
#include "Patron.h"
#include "Libraria.h"

std::string getId(std::string name)
{
    std::string id; //ВВід користувача для id обєкту

    std::cout << "What is the " << name << "'s ID?" << std::endl;

    //ігноруємо нажимання enter
    do
    {
        getline(std::cin, id);
    } while (id.empty());

    return id;
}

int main()
{
    char response; //відповідь користувача для меню
    Library bookshelf; //бібліотека з якою співпрацює користувач

    //отримування команд користувача, поки вони не захочуть припинити роботу
    do
    {
        std::cout << "Library Options:\n" << std::endl;
        std::cout << "1) add a book\n"
            << "2) add a member\n"
            << "3) check out a book\n"
            << "4) return a book\n"
            << "5) request a book\n"
            << "6) pay a fine\n"
            << "7) increment date\n"
            << "8) view member info\n"
            << "9) view book info\n"
            << "0) quit" << std::endl;
        std::cout << "\nWhat do you want to do?" << std::endl;
        std::cin >> response;
        std::cin.ignore(INT_MAX, '\n');

        std::cout << std::endl;
        switch (response)
        {
        case '1': bookshelf.addBook();
            break;
        case '2': bookshelf.addMember();
            break;
        case '3':
        {
            std::string bookId3 = getId("book");
            std::string memberId3 = getId("member");
            bookshelf.checkOutBook(memberId3, bookId3);
            break;
        }
        case '4':
        {
            std::string bookId4 = getId("book");
            bookshelf.returnBook(bookId4);
            break;
        }
        case '5':
        {
            std::string bookId5 = getId("book");
            std::string memberId5 = getId("member");
            bookshelf.requestBook(memberId5, bookId5);
            break;
        }
        case '6':
        {
            std::string memberId6 = getId("member");
            std::cout << "How much do you want to pay?" << std::endl;
            double payment;
            std::cin >> payment;
            std::cin.ignore(INT_MAX, '\n');
            bookshelf.payFine(memberId6, payment);
            break;
        }
        case '7':
        {
            bookshelf.incrementCurrentDate();
            break;
        }
        case '8':
        {
            std::string memberId8 = getId("member");
            bookshelf.viewPatronInfo(memberId8);
            break;
        }
        case '9':
        {
            std::string bookId9 = getId("book");
            bookshelf.viewBookInfo(bookId9);
            break;
        }
        case '0': break;
        default: std::cout << "That is not a valid option." << std::endl;
        }


        if (response != '0')
        {
            std::cout << "\nHit ENTER to go back." << std::endl;
            std::cin.get();
            system("cls");
        }

    } while (response != '0');

    return 0;
}