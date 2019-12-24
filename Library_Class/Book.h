#pragma once
#ifndef BOOK_H
#define BOOK_H

#include "Patron.h"
#include <string>
#include <vector>

//������� �����
enum Locale { ON_SHELF, ON_HOLD, CHECKED_OUT };

class Patron;

//����_1 �����
class Book
{
private:
    std::string idCode; //��������� �������������
    std::string title; //����� ������
    std::string author; //����� ������
    Locale location; //�� ����������� ������
    Patron* checkedOutBy; //������, ��� ����� �� �����
    Patron* requestedBy; //������, ��� ���� �����
    int dateCheckedOut; //ʳ������ ����, ��� ����� ����� � ���� �����
public:
    static const int CHECK_OUT_LENGTH = 14; //ʳ������ ���, �� ��������� ��� ��������� � ����
    //����������� �����
    Book();
    Book(std::string idc, std::string t, std::string a);

    std::string getIdCode() //��������� id_����
    {
        return idCode;
    }

    std::string getTitle() //��������� �����
    {
        return title;
    }

    std::string getAuthor() //��������� ������
    {
        return author;
    }

    Locale getLocation() //��������� ������������� �����
    {
        return location;
    }

    void setLocation(Locale lo) //������������ ������������� �����
    {
        location = lo;
    }

    Patron* getCheckedOutBy() //���������� ���������� �� �������, �� ����� �����
    {
        return checkedOutBy;
    }

    void setCheckedOutBy(Patron* p) //����������, �� ������ �� ���� ���� ��
    {
        checkedOutBy = p;
    }

    Patron* getRequestedBy() //���������� ���������� �� �������, ��  ��������� �����
    {
        return requestedBy;
    }

    void setRequestedBy(Patron* p) //����������, �� ������� �� ���� ��� ��
    {
        requestedBy = p;
    }

    int getDateCheckedOut() //��������� ������ ��� �� ������
    {
        return dateCheckedOut;
    }

    void setDateCheckedOut(int d) //������������ ������ ��� �� ������
    {
        dateCheckedOut = d;
    }
};

#endif // !BOOK_H


