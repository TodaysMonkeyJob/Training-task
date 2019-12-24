#pragma once
#ifndef LIBRARIA_H
#define LIBRARIA_H

#include <string>
#include<vector>
#include "Book.h"
#include "Patron.h"


//����_3 ���������
class Library
{
private:
    std::vector<Book> holdings; //������ ���� � ��������
    std::vector<Patron> members; //������ ������������ � ��������
    int currentDate; //���� � ����� ��������� ��������
    Patron* memberCheck(std::string patronID);//�������� �� id �����������
    Book* bookCheck(std::string bookID);//�������� �� id �����

public:
    double DAILY_FINE = 0.1;//������ �� ����
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
