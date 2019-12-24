#include "Patron.h"
#include "Libraria.h"


void Patron::removeBook(Book* b)
{//��� ����� ����� ����� � ������
    for (int i = 0; i < checkedOutBooks.size(); i++)
    {
        /*
        ���� ��� ����� ����� ���������� ����� � �����,
         �� ���������� �� � ��������,�� �������, ��� ������
         �� �� ������� ��� � ��������
         */
        if (checkedOutBooks[i]->getIdCode() == b->getIdCode())
            checkedOutBooks.erase(checkedOutBooks.begin() + i);
    }
}

/******************************************************************************
* ����: ���� �������� � ��������� �d �����������
*
* �����: ��������� ����������� � ��������� id � ������� �������� �� �����
*
* ����: ��������� ���������� ����������� � ������� ������������
******************************************************************************/
Patron* Library::memberCheck(std::string patronID)
{
    int memberPos = -1; // ������� ����������� � ��������� ID

    for (int i = 0; i < members.size(); i++)//��� ������� �����������
    {
        if (members[i].getIdNum() == patronID)//���� ��� ����������� ������� ����������
        {
            memberPos = i;//������� ���� �
        }
    }
    if (memberPos < 0)//���� ������� �����, �� �������
        return NULL;
    else
        return &members[memberPos];//��������� ������� ����������� �� ���� �������
}

