#pragma once
#ifndef PATRON_H
#define PATRON_H

#include "Book.h"
#include <string>
#include <vector>

class Book;
//����_2 ����������
class Patron
{
private:
    std::string idNum; //��������� �������������
    std::string name; //��� �����������
    std::vector<Book*> checkedOutBooks; //������, ��� ���������� ���� �� ����
    double fineAmount; //������ �������� �� �������� ���� � ����

public:
    Patron() //����������� �����������
    {
        fineAmount = 0;
    }

    Patron(std::string idn, std::string n) //���������� ���� ����������
    {
        idNum = idn, name = n, fineAmount = 0;
    }

    std::string getIdNum() //��������� �������� Id����
    {
        return idNum;
    }

    std::string getName() //��������� �������� ����
    {
        return name;
    }

    std::vector<Book*> getCheckedOutBooks() //��������� �������� ����, �� ���� ������������ 
    {
        return checkedOutBooks;
    }

    void addBook(Book* b) //��������� ����, �� ������ ������ �����������
    {
        checkedOutBooks.push_back(b);
    }

    void removeBook(Book* b);

    double getFineAmount() //��������� �������� ����� �� �����
    {
        return fineAmount;
    }

    void amendFine(double amount) //��������� �����,���� ���������� �����
    {
        fineAmount += amount;
    }
};

#endif // !PATRON_H
