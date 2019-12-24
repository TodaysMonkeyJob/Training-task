#include "Libraria.h"

#include <stdio.h>
#include <iostream>
#include <iomanip>

Library::Library()//����������� ��������
{
    currentDate = 0;//���� ��������
    holdings.reserve(100);//��������� ����
    members.reserve(100);//��������� ������������
}

/******************************************************************************
* ����: �������
*
* �����: ��������� ���������� ��� ����� � ��������� �� � ��������� ������
*
* ����: ��������� ����� � ��������
******************************************************************************/
void Library::addBook()
{
    std::string idCode, title, author; // ���������� ��� �����

    std::cout << "What is the book's ID code?" << std::endl;
    //���������� id �����
    getline(std::cin, idCode);

    //�������� �� Id �� ������������
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
    //���������� ���� ����� � ��������� �� � ��������� ������
    Book newBook(idCode, title, author);
    holdings.push_back(newBook);
}

/******************************************************************************
* ����: �������
*
* �����: ��������� ���������� ��� ������ ����������� � ���������
*       ���� � ��������� ������
*
* ����: ��������� ����������� � ��������
******************************************************************************/
void Library::addMember()
{
    std::string idCode, name; // ���������� ��� �����������

    std::cout << "What is the member's ID code?" << std::endl;
    //���������� id �����������
    getline(std::cin, idCode);

    //�������� ID �� ����������
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
    //���������� ������ ����������� � ��������� ���� � ��������� ������
    Patron newMem(idCode, name);
    members.push_back(newMem);
}


/******************************************************************************
* ����:  ��� ������������� �� ������, ���� �� �������� �����������,
*         �� ���� ����� ����� � ����� , �� ��������� �����, �� ������ �����
*
* �����: �������� �� ����� ���� ���� ����� ������������ � ���� ���
*        �� ������ ��������� ����� � �������� �� ����� �����������
*        � ������ ������ ����
*
* ����: ����� ����� � ��������
******************************************************************************/
void Library::checkOutBook(std::string patronID, std::string bookID)
{
    Patron* member = memberCheck(patronID); // �������� �� ����������� � ��������� ID
                        // ������� ���� �����
    Book* book = bookCheck(bookID); // �������� �� ������ � ��������� ID
                    // ������� ���� �����
    //�������� �� ���������� ���� ����� �����
    //�������� �� ���������� ����
    if (member == NULL)
    {
        std::cout << "\nThat is an invalid member ID." << std::endl;
    }//�������� �� ����� ����
    else if (book == NULL)
    {
        std::cout << "\nThat book is not a part of this library." << std::endl;
    }//�������� �� �� ��� �� ����� �� �����
    else if (book->getLocation() == 2)
    {
        std::cout << "\nThat book is already checked out." << std::endl;
    }//�������� �� �� �� ���� ����� �����
    else if (book->getLocation() == 1
        && book->getRequestedBy()->getIdNum() != member->getIdNum())
    {
        std::cout << "\nThat book is on hold by another member." << std::endl;
    }//���� �������� �� ��������
    else
    {
        //������������ ��������� ���������
        book->setCheckedOutBy(member);//����� �����������, �� ���� �����
        book->setDateCheckedOut(currentDate);//�������� ����
        book->setLocation(CHECKED_OUT);//���� ��������� �����, �� *�� �����*
        if (book->getLocation() == 1)//���� ����� �����
            book->setRequestedBy(NULL);//���� ��������� ������� �� �������
        member->addBook(book);//��������� ����� �����������
        std::cout << "\n" << book->getTitle() << " has been checked out by "
            << member->getName() << "." << std::endl;
    }
}

/******************************************************************************
* ����: ҳ���� ���� ��������, �� ����� �� id ��� ������
*
* �����: �������� �� ����� ���� ���� ��������� ������������ � ���� ���
*        �� ������ ��������� ����� � �������� �� ����� �����������
*        � ������ ������ ����
*
* ����: �������� ����� � ��������
******************************************************************************/
void Library::returnBook(std::string bookID)
{
    Book* book = bookCheck(bookID); // �������� �� ����� � ��������� ID
    // ������� ���� ����� �� ����
    if (book == NULL)
    {
        std::cout << "\nThat book is not a part of this library." << std::endl;
    }//���� ����� �� �����
    else if (book->getLocation() != 2)
    {
        std::cout << "\nThat book is not checked out." << std::endl;
    }
    else
    {//�������� �� �������, �� ����� ����� � ������ ������� ���������� �����
        Patron* member = book->getCheckedOutBy();
        member->removeBook(book);//

        if (book->getRequestedBy() != NULL)//���� ����� ����� ��������, 
            book->setLocation(ON_HOLD);   //�� ���� ��������� *�� �����*
        else
            book->setLocation(ON_SHELF);//� ������ ������� � ��������

        book->setCheckedOutBy(NULL);//�������� ����� ����� ������������ ����� ������
        std::cout << "\n" << book->getTitle() << " has been returned." << std::endl;
    }
}


/******************************************************************************
* ����:  ��� ������������� �� ������, ���� �� �������� �����������,
*         �� ���� ����� ����� � ����� , �� ��������� �����, �� ������ �����
*
* �����: �������� �� ����� ���� ���� ����� ������������ � ���� ���
*        �� ������ ��������� ����� �� ������ ������� �����������(requestedBy)
*
* ����: ����� �� ���������� ����� � ���� ����������
******************************************************************************/
void Library::requestBook(std::string patronID, std::string bookID)
{
    Patron* member = memberCheck(patronID); // �������� �� ����������� � ��������� ID
                        // ������� ���� �����
    Book* book = bookCheck(bookID); // �������� �� ����� � ��������� ID
    // ������� ���� ���������� �� ����
    if (member == NULL)
    {
        std::cout << "\nThat is not a valid member ID." << std::endl;
    }//������� ,���� ����� �� ����
    else if (book == NULL)
    {
        std::cout << "\nThat book is not a part of this library." << std::endl;
    }//���� ����� ������ �����
    else if (book->getRequestedBy() != NULL)
    {
        std::cout << "\nThat book is on hold by another member." << std::endl;
    }
    else
    {//���� ����� ������� ����� �� �����
        book->setRequestedBy(member);
        if (book->getLocation() == 0)// ���� ����������� ��������� �����
            book->setLocation(ON_HOLD);// �� ��������� �� �����
        std::cout << "\n" << book->getTitle() << " has been requested by "
            << member->getName() << "." << std::endl;
    }
}

/******************************************************************************
* ����: �������
*
* �����: ������ ������� ��� �� ����� �������� ���� �������� � ����
*        �� ����������������(fineAmount) ������� �����������, �� ���������
*     �������� ����� � ����
*
* ����: ���� ���� � ����������� �� ��������� ����� �� �������
******************************************************************************/
void Library::incrementCurrentDate()
{
    currentDate++;//��������� ��������� ���
    for (int i = 0; i < holdings.size(); i++)//��� ������� ���������� ���
    {
        if (holdings[i].getLocation() == 2 &&//��� ��� ��� �� ����� *�� �����*
            ((currentDate - holdings[i].getDateCheckedOut()) > Book::CHECK_OUT_LENGTH))//� � ��� ������ ��� �������� ����� � ����
        {
            holdings[i].getCheckedOutBy()->amendFine(DAILY_FINE);//�������� �������� �������������
        }
    }
    std::cout << "The date is now " << currentDate << "." << std::endl;
}

/******************************************************************************
* ����: ��� ���������, ���� �� ������ � id �����������, ���� ���� ���������
*       �������������, � ���� double � ����� ������� ���� �������
*
* �����: ������ ������������� ����������� � ����� �������
*
* ����: �������� �������������
******************************************************************************/
void Library::payFine(std::string patronID, double payment)
{
    Patron* member = memberCheck(patronID); // �������� �� ����������� � ��������� ID
    // ������� ���� ����������� �� ����
    if (member == NULL)
    {
        std::cout << "\nThat is an invalid member ID" << std::endl;
    }
    else
    {//���������� �����
        member->amendFine(0 - payment);
        std::cout << "\nThe fines for " << member->getName()//������������� ��� �����������
            << " are now $" << std::fixed << std::showpoint << std::setprecision(2)//������+������� �������+
            << member->getFineAmount() << "." << std::endl;//+���������� �������������
    }
}


/******************************************************************************
* ����: ���� �������� � ��������� �d �����������
*
* �����: ���� ���������� ��� ����������� � ��������� ���� id
*
* ����: ���� ���������� ��� �����������
******************************************************************************/
void Library::viewPatronInfo(std::string patronID)
{
    Patron* member = memberCheck(patronID); // �������� �� ����������� � ��������� ID
                        // ������� ���� �����
    std::string line;
    //���� ��������������� ��� ����� ��
    line.assign(20, '-');
    //
    if (member == NULL)
    {
        std::cout << "\nThe is an invalid member ID" << std::endl;
    }
    else
    {
        std::cout << std::left << std::setw(16) << "\nID NUMBER:" << member->getIdNum()//��������� �d �����������
            << "\n" << std::endl;
        std::cout << std::setw(15) << "NAME:" << member->getName() << std::endl;//��������� ���� �����������
        std::cout << std::setw(15) << "\nCHECKED OUT BOOKS:" << std::endl;//����, �� �� ����
        std::cout << line << std::endl;
        for (int i = 0; i < member->getCheckedOutBooks().size(); i++)//��� ����� ����� �����
        {
            std::cout << std::setw(20) << member->getCheckedOutBooks()[i]->getTitle()//����� �����
                << std::endl;
            std::cout << line << std::endl;
        }
        std::cout << "\nCURRENT FINES: $" << std::fixed << std::showpoint << std::setprecision(2)//������������� �����������
            << member->getFineAmount() << std::endl;
    }
}

/******************************************************************************
* ����: ���� �������� � ��������� �d �����
*
* �����: ���� ���������� ��� ����� � ��������� �� id
*
* ����: ���� ���������� ��� �����
******************************************************************************/
void Library::viewBookInfo(std::string bookID)
{
    Book* book = bookCheck(bookID); // �������� �� ����� � ��������� ID
    // ������� ���� �����
    if (book == NULL)
    {
        std::cout << "\nThat book is not a part of this library" << std::endl;
    }
    else
    {//��������� ���������� ��� �����
        std::cout << std::left << std::setw(21) << "\nID CODE:" << book->getIdCode()
            << "\n" << std::endl;
        std::cout << std::setw(20) << "TITLE:" << book->getTitle() << "\n" << std::endl;
        std::cout << std::setw(20) << "AUTHOR" << book->getAuthor() << "\n" << std::endl;
        std::cout << std::setw(20) << "LOCATION";
        //���������� ��� �� ���������
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
            std::cout << std::setw(20) << "CHECKED OUT BY:" << book->getCheckedOutBy()->getName()//��� ���� ��� ����
                << "\n" << std::endl;
            std::cout << std::setw(20) << "DUE DATE:"
                << (book->getDateCheckedOut() + book->CHECK_OUT_LENGTH) << "\n"//ʳ������ ��� ����� *�� �����*
                << std::endl;
        }
        if (book->getRequestedBy() != NULL)//���� ����� ����� �����
        {
            std::cout << std::setw(20) << "REQUESTED BY:" << book->getRequestedBy()->getName()//�������� ��� ���� �����
                << std::endl;
        }
    }
}


