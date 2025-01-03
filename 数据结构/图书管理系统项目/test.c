#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

/*�궨����*/ 
#define  ADMIN_password "123456" /*����Ա��¼����*/

//�鼮��Ϣ
typedef struct book 
{
    char id[50];       //���
    char name[50];    //����
    char author[50];   //����
    char press[50];    //������
    char category[50]; //����
    double price;       //�۸�
} BOOKINFO;
int library_quantity = 0;

//��Ա����鼮��Ϣ
typedef struct book_loans
{
    char id[50];       //���
    char name[50];    //����
    char author[50];   //����
    char press[50];    //������
    char category[50]; //����
    double price;       //�۸�
    char member_id[50];//��Ա���
} BOOKLOANS;
int book_loans = 0;//�ܵ��鼮������

//��Ա��Ϣ
typedef struct member 
{
    char id[50];       //�˻�
    char password[50]; //����
    char name[50];     //����
    char sex[10];      //�Ա�
    char phone[12];    //�ֻ���
} MEMBERINFO;
int member_number = 0;

/*�˵�������*/
void menu1();
void menu2();
void menu3();

/*���ߺ�����*/
int compare_password(char password[20]);/*����ȶԺ��� */  
void clock_delay(); /*ʱ����ʱ����*/ 
void password_circle();/*�����װ�κ���*/
int is_library_empty();/*�ж�������Ƿ���ͼ����Ϣ*/

/*��Ա��Ϣϵͳ�㼶������*/
int user_account(char account[20]);/*�����˻���Ϣ*/ 
void member_login_up();/*��Աע�ắ��*/
int member_login_in(char account[20]);/*��Ա��¼����*/ 
void ADMIN_watch_member();/*�鿴��Ա��Ϣ����*/
void display_memberbook();/*�鿴����ͼ�������Ϣ����*/
int check_repeat_id(char id[30]);/*����˻��ظ��Ժ���*/ 

/*ͼ����Ϣϵͳ�㼶������*/
void add_book();/*�����½���ͼ����Ϣ*/
void delete_book();/*����ͼ�����ƶ�ͼ����Ϣ����ɾ��*/
void modify_book();/*�޸�ͼ����Ϣ*/
void display_book();/*��ʾȫ��ͼ����Ϣ*/
void search_book();/*����ͼ��������ʾͼ�����Ϣ*/
void borrow_book(char account[20]);/*����*/
void return_book(char account[20]);/*����*/
int check_repeat_book(char number[30]);/*�����鼮���*/

int main()
{
    int flag1=1,flag2=1,flag3=1;/* flag���ж�����,flagΪ 1 ʱΪ�棬Ϊ 0 ʱΪ�� */
	char choice;
	FILE *p1,*p2,*p3;

    system("title ͼ�����ϵͳ");
    system("color E9");

    if((p1 = fopen("library.txt","r")) == NULL) { 
        p1 = fopen("library.txt","w"); /*p1,�鼮��Ϣ�ļ�ָ��*/
        fclose(p1);
    }
    if((p2 = fopen(".txt","r")) == NULL) {
        p2 = fopen("infomember.txt","w"); /*p2,��Ա������Ϣ�ļ�ָ��*/ 
        fclose(p2);
    }
    if((p3 = fopen("memberbook.txt","r")) == NULL) {
        p3 = fopen("memberbook.txt","w"); /*p3,��Ա�����鼮��Ϣ�ļ�ָ��*/ 
        fclose(p3);
    }
    while (1)
    {
        system("cls");
		menu1();/*�������˵� */ 

  		printf("\n");
        printf("\t\t\t����������Ҫִ�еĹ���(1-4):");
        choice=getchar();
  		while(choice!='1'&&choice!='2'&&choice!='3'&&choice!='4'&&choice!='5') {
            choice=getchar();
        }
  		fflush(stdin);

        if(choice == '1') {
            /*��Ա����*/
            int flag=0;
			char account[20],account_choice;
			system("cls");
			password_circle();
            gets(account);
            flag = member_login_in(account); /*��¼*/ 
            /*ûע��Ļ����ע�ắ��*/

            if(flag == 2) { //ûע�ᣬע���������µ�¼
                system("cls");
				password_circle();
				fflush(stdin);
				gets(account);
				flag=member_login_in(account);
            }

            if(flag == 1) {
                while (flag2 && flag3)
                {
                    system("cls");
                    
                    menu2();
                    
                    printf("\t\t\t����ѡ��(1-6):");
                    account_choice=getchar();
                    while(account_choice!='1'&&account_choice!='2'&&account_choice!='3'&&account_choice!='4'&&account_choice!='5'&&account_choice!='6'&&account_choice!='7') {
                        account_choice=getchar();
                    }

                    switch (account_choice)
                    {
                        case '1':search_book(); break;
                        case '2':borrow_book(account); break;
                        case '3':return_book(account); break;
                        case '4':display_book(); break;
                        case '5':if(user_account(account))
                                    {
                                        printf("\n\n��¼��Ϣ�ı�,�����µ�¼...");
                                        clock_delay();
                                        flag3=0;
                                    }
                                break;
                        case '6':
                                printf("\n\n\t\t\t�����˳��û�����...");
                                clock_delay();
                                flag2 = 0;
                                break;
                        default:
                            break;
    				}
                }
                flag2 = flag3 = 1;
            }

        } else if(choice == '2') {
            /*��Աע��*/
            system("cls");
			printf("\n\n\n\t\t\t���ڽ����û�ע�����...");
			clock_delay();
     	    member_login_up();
        } else if(choice == '3') {
            /*����Ա��¼*/
            if(compare_password(ADMIN_password)) { 
                printf("\n\n\t\t\t\t  --����������ȷ!--\n\n\t\t\t\t==���ڽ������Ա����==\n");
     	  	 	clock_delay(); 
                char manager_choice;
                while(flag2) {
                    system("cls");
                    menu3();
                    printf("\n");

                    printf("\t\t\t����ѡ��(1-8):");
                    manager_choice=getchar();
                    while(manager_choice!='1'&&manager_choice!='2'&&manager_choice!='3'&&manager_choice!='4'&&manager_choice!='5'&&manager_choice!='6'&&manager_choice!='7'&&manager_choice!='8')
                        manager_choice=getchar();
            
                    switch(manager_choice)
                    {
                        case '1':add_book(); break;
                        case '2':delete_book(); break;
                        case '3':modify_book(); break;
                        case '4':search_book(); break;
                        case '5':display_book(); break;
                        case '6':ADMIN_watch_member();break; 
                        case '7':display_memberbook();break;
                        case '8':flag2=0;
                                printf("\n\n\t\t\t�����˳�����Ա����...");
                                clock_delay();
                                break;
                        default:
                            break;
                    }
  				}
            } else {
                printf("\n\n\t\t\t\t  --�����������!--\n");
     		   	clock_delay();
            }
        } else {
            /*�˳�ϵͳ*/
            break;
        }
    }

    fflush(stdin);
	system("cls");
    printf("���Ѱ�ȫ���˳�ϵͳ!\n(��������رս���)");
    printf("��ӭ�����´�ʹ��!\n");
    getchar();
    return 0;
}




/*�˵�������*/

void menu1()
{
	system("color E9");
	printf("\n\n");
	printf("\t\t\t *=======================================*\n");
	printf("\t\t\t|  * - * - * ͼ�����ϵͳ * - * - *  |\n");
	printf("\t\t\t| *                                     * |\n");
	printf("\t\t\t| |  [1]   ��Ա��¼                     | |\n");
	printf("\t\t\t| *                                     * |\n");
	printf("\t\t\t| |  [2]   ��Աע��                     | |\n");
	printf("\t\t\t| *                                     * |\n");
	printf("\t\t\t| |  [3]   ����Ա��¼                   | |\n");
	printf("\t\t\t| *                                     * |\n");
	printf("\t\t\t| |  [4]   �˳�ϵͳ                     | |\n");
	printf("\t\t\t| *                                     * |\n");
	printf("\t\t\t|  * - * - * - * - * - * - * - * - * - *  |\n");
	printf("\t\t\t *=======================================*\n");
}

void menu2()
{
	system("color F9");
	printf("\n\n");
	printf("\t\t\t *=====================================*\n");
    printf("\t\t\t| | * - * - * -��-Ա-��-��- * - * - * | |\n");
    printf("\t\t\t| *                                   * |\n");
    printf("\t\t\t| |  [1]   ����ͼ����Ϣ               | |\n");
    printf("\t\t\t| *  [2]   ����ͼ��                   * |\n");
    printf("\t\t\t| |  [3]   �黹ͼ��                   | |\n");
    printf("\t\t\t| *  [4]   �������ͼ����Ϣ           * |\n");
    printf("\t\t\t| |  [5]   �����˻���Ϣ               | |\n");
    printf("\t\t\t| *  [6]   �˳��û�����               * |\n");
    printf("\t\t\t| |                                   | |\n");
    printf("\t\t\t| * - * - * - * - * - * - * - * - * - * |\n");
	printf("\t\t\t *=====================================*\n");
}

void menu3()
{
	system("color F9");
	printf("\n\n");
	printf("\t\t\t *======================================*\n");
	printf("\t\t\t| | * - * - * ��-��-Ա-��-�� * - * - * | |\n");
	printf("\t\t\t| *                                    * |\n");
	printf("\t\t\t| |  [1]   ���ͼ��                    | |\n");
	printf("\t\t\t| *  [2]   ɾ��ͼ��                    * |\n");
	printf("\t\t\t| |  [3]   �޸�ͼ����Ϣ                | |\n");
	printf("\t\t\t| *  [4]   ����ͼ����Ϣ                * |\n");
	printf("\t\t\t| |  [5]   ��ʾȫ��ͼ����Ϣ            | |\n");
	printf("\t\t\t| *  [6]   ��ʾ���л�Ա��Ϣ            * |\n");
	printf("\t\t\t| |  [7]   ��ʾ���н�����Ϣ            | |\n");
	printf("\t\t\t| *  [8]   �˳�����Ա����              * |\n");
	printf("\t\t\t| |                                    | |\n");
	printf("\t\t\t| * - * - * - * - * -- * - * - * - * - * |\n");
	printf("\t\t\t *======================================*\n");
}

/*���ߺ�����*/

/*ʱ����ʱ����*/
#include <time.h>

void clock_delay()
{
    clock_t start_time = clock();
    // 1�� = CLOCKS_PER_SEC��ʱ������
    // 1000���� = CLOCKS_PER_SEC / 1000��ʱ������
    while ((clock() - start_time) < (CLOCKS_PER_SEC / 1000) * 1000);
}


/*�����װ�κ���*/
void password_circle()
{
	system("cls");
	printf("\n\n\n\t\t\t***================================*** \n");
	printf("\t\t\t                                   \n");
	printf("\t\t\t   �˻� (account):");
}

/*�ж������û���κ��鼮��Ϣ*/
int is_library_empty(int library_quantity)
{
	if(!library_quantity) {
		printf("�����û���κ��鼮��Ϣ��\n");
        printf("��������������˵���");
        getchar();
		return 1;
	}
	return 0;
}


/*ͼ����Ϣϵͳ�㼶������*/

//�����鼮���
int check_repeat_book(char id[30]) 
{
    BOOKINFO books[200];
    FILE *p1;
    int i;
    library_quantity = 0;
    p1 = fopen("library.txt","r");
    while(fscanf(p1, "%s %s %s %s %s %lf",books[library_quantity].id, books[library_quantity].name, books[library_quantity].author,
                  books[library_quantity].press, books[library_quantity].category,&books[library_quantity].price) == 6)
    {
        library_quantity++;
    }
    fclose(p1);
    
    for(i = 0;i < library_quantity;i++) {
        if(strcmp(books[i].id,id) == 0) {
            return 1;
        }
    }
    return 0;
}

void add_book()
{
    BOOKINFO newbook;
    FILE* p1;
    char choice1,choice2;//choice1,�Ƿ񱣴���ӵ��鼮,choice2,�Ƿ�������ͼ����Ϣ
    system("cls");
    /*���鼮�Ѿ�����ӵ������*/
    /*�ɹ������鼮��Ϣ*/
    /*û�����鼮��Ϣ*/
    while(1) {
        
        fflush(stdin);
        printf("��������Ҫ��ӵ��鼮��ţ�");
        gets(newbook.id);

        if(check_repeat_book(newbook.id)) 
        {
            printf("���鼮�Ѿ�����ӵ�����С�\n");
            getchar();
        } else {
            fflush(stdin);
            printf("����������:");
			gets(newbook.name);
		
			printf("����������:");
			gets(newbook.author);
		
			printf("�����������:");
			gets(newbook.press);
			
			printf("���������(��ѧ/��ѧ/��ѧ/��ѧ/��):");
			gets(newbook.category);
		
			printf("������۸�:");
			scanf("%lf",&newbook.price);

            fflush(stdin);

            printf("�Ƿ񱣴���鼮��Ϣ(Y/N):");
            choice1 = getchar();
            while(choice1 != 'Y' && choice1 != 'N') {
                choice1 = getchar(); 
            }

            if(choice1 == 'Y') {
                p1 = fopen("library.txt","a");
                fprintf(p1,"%s %s %s %s %s %lf\n",
                    newbook.id,newbook.name,newbook.author,
                    newbook.press,newbook.category,newbook.price);
                fclose(p1);
                printf("�Ѿ��ɹ������µ��鼮��Ϣ��\n");
            } else {
                printf("δ������鼮��Ϣ��\n");
            }
        }

        printf("�Ƿ�������ͼ����Ϣ?(Y/N):");
        choice2 = getchar();
        while(choice2 != 'Y'&& choice2 != 'N') {
            choice2 = getchar();
        }
        if(choice2 == 'N') {
            break;
        }

    }
}

void delete_book()
{
    char delete_book[20] = ""; //�������Ҫɾ��������
    BOOKINFO books[200];
    FILE *p1;
    char choice1,choice2;
    int i;
    system("cls");

    while (1)
    {
        fflush(stdin);
        printf("������Ҫɾ��������:");
        gets(delete_book);

        library_quantity = 0;
        p1 = fopen("library.txt","r");
        while(fscanf(p1, "%s %s %s %s %s %lf",books[library_quantity].id, books[library_quantity].name, books[library_quantity].author,
                    books[library_quantity].press, books[library_quantity].category,&books[library_quantity].price) == 6)
        {
            library_quantity++;
        }
        fclose(p1);
        is_library_empty(library_quantity);

        for(i = 0;i < library_quantity;i++) {
            if(strcmp(books[i].name,delete_book) == 0) { 
                break;
            } 
        }

        if(i >= library_quantity) { 
            printf("�����û�С�%s�����鼮��Ϣ��\n",delete_book);
        } else {
            printf("�Ƿ�ɾ����%s�����鼮��Ϣ?(Y/N):",delete_book);
            choice1 = getchar();
            while (choice1 != 'Y' && choice1 != 'N') {
                choice1 = getchar();
            }
            if(choice1 == 'Y') {
                for(;i < library_quantity;i++) { //Խ����ô����?
                    books[i] = books[i+1];
                }
                p1=fopen("library.txt","w");
                for(i = 0;i < library_quantity;i++) {
                    fprintf(p1,"%s %s %s %s %s %lf\n",
                        books[i].id, books[i].name, books[i].author,
                        books[i].press, books[i].category, books[i].price);
                }
               	fclose(p1);
                library_quantity--;
                printf("�ѳɹ�ɾ����%s�����鼮��Ϣ��\n",delete_book);
            } else {
                printf("��%s�����鼮��Ϣû�б�ɾ����\n",delete_book);
            }
        }

        printf("�Ƿ��������ɾ������?(Y/N):"); //�û�ûִ��ɾ��������û���ҵ�Ҫɾ�����鼮
        choice2 = getchar();
        while (choice2 != 'Y' && choice2 != 'N') {
            choice2 = getchar();
        }
        if(choice2 == 'N') {
            break;
        }
    }
}

/*�޸��鼮��Ϣ*/
void modify_book()
{
    char id[50];       //���
    char name[50];     //����
    char author[50];   //����
    char press[50];    //������
    char category[50]; //����
    double price;      //�۸�

    char search_name[30]; //Ҫ�޸ĵ�����
    char change; //Ҫ�޸ĵ��鼮��Ϣ���
    FILE *p1;
    BOOKINFO books[200];
    char choice1, choice2;
    int i;
    int flag1; // flag1 = 1,û�ҵ�Ҫ�޸ĵ�ͼ����Ϣ�������޸���һ��ͼ����Ϣ
    int flag2; // flag2 = 1,Ҫ�޸ĵ�ͼ����Ϣ�������Ϣ�ظ�
    system("cls");

    while (1)
    {
        flag1 = 0;
        flag2 = 0;
        
        fflush(stdin);

        library_quantity = 0;
        p1 = fopen("library.txt","r");
        while(fscanf(p1, "%s %s %s %s %s %lf",books[library_quantity].id, books[library_quantity].name, books[library_quantity].author,
                    books[library_quantity].press, books[library_quantity].category,&books[library_quantity].price) == 6)
        {
            library_quantity++;
        }
        fclose(p1);
        is_library_empty(library_quantity);

        fflush(stdin);
        printf("������Ҫ�޸���Ϣ���鼮��: ");
        gets(search_name);

        for (i = 0; i < library_quantity; i++) {
            if (strcmp(books[i].name, search_name) == 0) {
                break;
            }
        }

        if (i >= library_quantity) {
            printf("δ�ҵ���%s�����鼮��Ϣ��\n", search_name);
            flag1 = 1;
        } else {
            printf("\n"); 
            printf("|---------------------------------ͼ����Ϣ----------------|\n");
            printf("|���  ����        ����      ������          ���    ����  |\n");
            printf("|                                                                          |\n");
            printf("|%-6s%-12s%-10s%-16s%-8s%-8.1f|\n",
                books[i].id, books[i].name, books[i].author,
                books[i].press, books[i].category, books[i].price);

            while (1)
            {
                printf("�����޸ĵ��鼮��Ϣ��?\n");
                printf("1.���\n2.����\n3.����\n4.������\n5.���\n6.����\n");
                printf("����ѡ����: ");
                change = getchar();
                while (change < '1' || change > '6')
                {
                    change = getchar();
                }
                fflush(stdin);
                printf("�������µĴ���: ");
                switch (change)
                {
                case '1':
                    gets(id);
                    flag2 = check_repeat_book(id); 
                    if (!flag2) {
                        strcpy(books[i].id, id);
                        flag1 = 1;
                    }
                    break;
                case '2':
                    gets(name);
                    strcpy(books[i].name, name);
                    flag1 = 1;
                    break;
                case '3':
                    gets(author);
                    strcpy(books[i].author, author);
                    flag1 = 1;
                    break;
                case '4':
                    gets(press);
                    strcpy(books[i].press, press);
                    flag1 = 1;
                    break;
                case '5':
                    gets(category);
                    strcpy(books[i].category, category);
                    flag1 = 1;
                    break;
                case '6':
                    scanf("%lf", &price);
                    books[i].price = price;
                    flag1 = 1;
                    fflush(stdin);
                    break;
                }

                if (flag2) {
                    printf("��Ҫ�޸ĵ�ͼ����Ϣ�������Ϣ�ظ�!\n");
                    break;
                } else {
                    printf("�Ƿ�����޸ġ�%s��ͼ����Ϣ?(Y/N):", search_name);
                    fflush(stdin);
                    choice2 = getchar();
                    while (choice2 != 'Y' && choice2 != 'N')
                    {
                        choice2 = getchar();
                    }
                    if (choice2 == 'N') {
                        break;
                    }
                }
            }
        }

        //��������Ҫ�޸ĵ�ͼ����Ϣ��1,û�ҵ�ͼ��,2,�����޸���һ��ͼ����Ϣ,3,Ҫ�޸ĵ�ͼ����Ϣ�������Ϣ�ظ�
        if (flag1 || flag2) {
            printf("�Ƿ�����޸�ͼ����Ϣ?(Y/N):");
            fflush(stdin);
            choice1 = getchar();
            while (choice1 != 'Y' && choice1 != 'N')
            {
                choice1 = getchar();
            }
            if (choice1 == 'N') {
                p1 = fopen("library.txt","w");
                for(i = 0;i < library_quantity;i++) {
                    fprintf(p1,"%s %s %s %s %s %lf\n",books[i].id,books[i].name,books[i].author,
                        books[i].press,books[i].category,books[i].price);
                }
                fclose(p1);

                printf("�Ѿ��ɹ������µ��鼮��Ϣ��\n");
                break;
            }
        }
    }
}

/*����ͼ��������ʾͼ�����Ϣ*/
void search_book()
{
    char search[30] = "";  // ��Ҫ���ҵ��ֶηŵ��������У�����Ϊid,name,author
    char compare[30] = ""; // ������е��ֶηŵ���������
    BOOKINFO books[200];
    FILE *p1;
    char choice1, choice2; 
    // choice1,����ѡ����ʲô�ֶβ�ѯ
    // choice2,�����Ƿ������ѯ
    int flag1; // flag1 = 1����ѯ���ֶ�������,һλ���߿��Զ�Ӧ�౾������
    int flag2; // flag2 = 1���Ƿ��ѯ������Ҫ����鼮
    int i;

    system("cls");
    fflush(stdin);

    library_quantity = 0;
    p1 = fopen("library.txt","r");
    while(fscanf(p1, "%s %s %s %s %s %lf",books[library_quantity].id, books[library_quantity].name, books[library_quantity].author,
                books[library_quantity].press, books[library_quantity].category,&books[library_quantity].price) == 6)
    {
        library_quantity++;
    }
    fclose(p1);
    is_library_empty(library_quantity);

    while (1) {
        printf("����ͨ�����ַ�ʽ��ѯ�鼮?\n");
        printf("1.���\n2.����\n3.����\n");
        choice1 = getchar();
        while (choice1 != '1' && choice1 != '2' && choice1 != '3') {
            choice1 = getchar();
        }

        printf("��������ҵ��ֶ���Ϣ: ");
        fflush(stdin);
        gets(search);
        flag1 = 1; 
        flag2 = 0;

        for (i = 0; i < library_quantity; i++) {
            switch (choice1) {
            case '1':
                strcpy(compare, books[i].id); 
                flag1 = 0; break;
            case '2':
                strcpy(compare, books[i].name); 
                flag1 = 0; break;
            case '3':
                strcpy(compare, books[i].author); 
                break;
            default:
                break;
            }

            if (strcmp(search, compare) == 0) {
                printf("|--------------------------ͼ����Ϣ-------------------------|\n");
      			printf("|���  ����        ����      ������          ���    ����   |\n");
      			printf("|                                                           |\n");
                printf("|%-6s%-12s%-10s%-15s%-8s%-8.1f|\n",
                       books[i].id, books[i].name, books[i].author,
                       books[i].press, books[i].category, books[i].price);
                flag2 = 1;
                if (!flag1) { // flag1 = 1����ѯ�ֶ�������
                    break;
                }
            }
        }

        if (!flag2) {
            printf("û���ҵ�������Ҫ����鼮!\n");
        }

        printf("�Ƿ������ѯ?(Y/N):");
        choice2 = getchar();
        while (choice2 != 'Y' && choice2 != 'N') {
            choice2 = getchar();
        }
        if (choice2 == 'N') {
            break;
        }
        fflush(stdin);
    }
}

void borrow_book(char account[20]) 
{
    BOOKINFO books[200];
    FILE *p1,*p3;
    char search[30];
    char choice;
    int flag;
    int i;

    system("cls");
    fflush(stdin);
    
    library_quantity = 0;
    p1 = fopen("library.txt","r");
    while(fscanf(p1, "%s %s %s %s %s %lf",books[library_quantity].id, books[library_quantity].name, books[library_quantity].author,
                books[library_quantity].press, books[library_quantity].category,&books[library_quantity].price) == 6)
    {
        library_quantity++;
    }
    fclose(p1);
    is_library_empty(library_quantity);

    while (1)
    {
        printf("������Ҫ����鼮����:\n");
        fflush(stdin);
        gets(search);

        for(i = 0;i < library_quantity;i++) {
            if(strcmp(books[i].name,search) == 0) {
                break;
            }
        }
            
        if(i >= library_quantity) {
            printf("�����û�С�%s�����鼮��Ϣ��\n",search); //�Ƿ��������
        } else {
            library_quantity--;

            p3=fopen("memberbook.txt","a");
            fprintf(p3,"%s %s %s %s %s %f %s\n",
                    books[i].id,books[i].name,books[i].author,books[i].press,
                    books[i].category,books[i].price,account);
            fclose(p3); 

            printf("����ɹ�!\n"); /*�������*/
        }
        
        printf("���Ƿ��������?(Y/N):");
        choice = getchar();
        while (choice != 'Y' && choice != 'N')
        {
            choice = getchar();
        }
        if(choice == 'N') {
            break;
        }
    }

    
}

void return_book(char account[20]) 
{
    FILE *p3;
	BOOKLOANS bookgrasp[100];
	char search[30];
    char choice;
    int i;
    int book_loans = 0;//�ܵı�����鼮����
	int member_loans = 0;//���û������鼮����
    int memberbooks[30]; //�û������鼮��bookgrasp�е������±�

	system("cls");
    fflush(stdin);

    p3= fopen("memberbook.txt", "r");
    while (fscanf(p3, "%s %s %s %s %s %lf %s", bookgrasp[book_loans].id, bookgrasp[book_loans].name, bookgrasp[book_loans].author, bookgrasp[book_loans].press,
                bookgrasp[book_loans].category, &bookgrasp[book_loans].price,bookgrasp[book_loans].member_id) != EOF) {
        book_loans++;  //���еĽ�����Ϣ
    }
    fclose(p3);

    for(i = 0;i < book_loans;i++) {
        if(strcmp(bookgrasp[member_loans].member_id,account) == 0) {
            memberbooks[member_loans++] = i; //���û��Ľ�����Ϣ
        }
    }

    if(member_loans <= 0) {
        printf("��û���κν�����Ϣ��\n");
        printf("�밴��������ء�\n");
        getchar();  //��ֹ
    } else {
        printf("�������ĵ�����ͼ����Ϣ����:\n"); 
        printf("|----------------------------ͼ�������Ϣ--------------------|\n");
        printf("|���  ����        ����      ������          ���    ����    |\n");
        for(i = 0;i < member_loans;i++) {
            int ret = memberbooks[i];
            printf("|%-6s%-12s%-10s%-16s%-8s%-8.1f|\n",bookgrasp[ret].id,
                        bookgrasp[ret].name,bookgrasp[ret].author,bookgrasp[ret].press,
                        bookgrasp[ret].category,bookgrasp[ret].price);
        }
        
        while (1)
        {
            printf("\n����Ҫ�黹���鱾��:\n");
            gets(search);
            fflush(stdin);

            int j; //��j�����ҵ���search
            for(j = 0;j < member_loans;j++) {
                int ret = memberbooks[j];
                if(strcmp(bookgrasp[ret].name,search) == 0) { 
                    break;
                }
            }

            if(j >= member_loans) {
                printf("��û������������Ϣ!��˶�������\n");
            } else {
                book_loans--;
                for(i = memberbooks[j];i < book_loans;i++) {
                    bookgrasp[i] = bookgrasp[i+1];  //����Խ��
                }
                member_loans--;
                for(i = j;i < member_loans;i++) {
                    memberbooks[i] = memberbooks[i+1]; //����Խ��
                }
                printf("����ɹ�!\n");
            }

            printf("�Ƿ��������?(Y/N):");
            choice = getchar();
            while (choice != 'Y' && choice != 'N')
            {
                choice = getchar();
            }
            if(choice == 'N') {
                p3 = fopen("memberbook.txt","w");
                for(i = 0;i < book_loans;i++) {
                    fprintf(p3, "%s %s %s %s %s %lf %s\n", bookgrasp[i].id, bookgrasp[i].name, bookgrasp[i].author, bookgrasp[i].press,
                            bookgrasp[i].category, bookgrasp[i].price,bookgrasp[i].member_id);
                }
                fclose(p3);
                break;
            }
        }
    }
    
}

/*��ʾȫ��ͼ����Ϣ*/
void display_book()
{
    FILE *p1;
    BOOKINFO books[200];
    int i;

    system("cls");
    fflush(stdin);

    library_quantity = 0;
    p1 = fopen("library.txt","r");
    while(fscanf(p1, "%s %s %s %s %s %lf",books[library_quantity].id, books[library_quantity].name, books[library_quantity].author,
                books[library_quantity].press, books[library_quantity].category,&books[library_quantity].price) == 6)
    {
        library_quantity++;
    }
    fclose(p1);
    is_library_empty(library_quantity);

    
    
    printf("\t\t\t����й���%d���顣\n", library_quantity);
    printf("|------------------------ͼ����Ϣ-------------------------|\n");
    printf("|���  ����        ����      ������          ���    ����  |\n");
    printf("|                                                        |\n");
    for (i = 0; i < library_quantity; i++) {
        printf("|%-6s%-12s%-10s%-16s%-8s%-8.1f|\n",
               books[i].id, books[i].name, books[i].author,
               books[i].press, books[i].category, books[i].price);
    }

    printf("\n�������������һ����\n");
    getchar();
    fflush(stdin);
}

/*��Ա��Ϣϵͳ�㼶*/

/*�����˻���Ϣ*/ 
int user_account(char account[20])  
{
    MEMBERINFO members[200];
    BOOKLOANS bookgrasp[200]; //��Ա����鼮��Ϣ��
    int loans_pos[100]; //���ڴ���û��������BOOKLOANS books�е������±�
    int totally_borrow = 0; //�û�������������/��������
    char old_password[30];
    char new_password1[30];
    char new_password2[30];
    char choice1; //�Ƿ��޸�����
    char choice2; //�Ƿ�����޸�����
    FILE *p2, *p3;
    int i; 

    system("cls");

    member_number = 0;
    p2 = fopen("infomember.txt", "r");
    while (fscanf(p2, "%s %s %s %s %s", members[member_number].id, members[member_number].password,
               members[member_number].name, members[member_number].sex, members[member_number].phone) == 5)
    {
        member_number++;
    }
    fclose(p2);

    book_loans = 0;
    p3 = fopen("memberbook.txt", "r");
    while (fscanf(p3, "%s %s %s %s %s %lf %s", bookgrasp[book_loans].id, bookgrasp[book_loans].name, bookgrasp[book_loans].author,
                  bookgrasp[book_loans].press, bookgrasp[book_loans].category, &bookgrasp[book_loans].price, bookgrasp[book_loans].member_id) == 7)
    {
        book_loans++;
    }
    fclose(p3);

    for (i = 0; i < member_number; i++) {
        if (strcmp(members[i].id, account) == 0) {
            break;
        }
    }

    if (i >= member_number) {
        printf("δ�ҵ��û���Ϣ��\n");
        return 0;
    }

    printf("\n");
    printf("|---------------------------������Ϣ-----------------------------------|\n");
    printf("|����        �Ա�      ID              ����             �ֻ���         |\n");
    printf("|%-12s%-10s%-16s%-17s%-15s|\n",members[i].name, members[i].sex, members[i].id, members[i].password, members[i].phone);
    printf("|                                                                      |\n");
    printf("|----------------------------------------------------------------------|\n");

    for (int j = 0; j < book_loans; j++) {
        if (strcmp(bookgrasp[j].member_id, account) == 0) {
            loans_pos[totally_borrow++] = j;
        }
    }

    if (totally_borrow <= 0) {
        printf("����ͼ�����û���κν�����Ϣ��\n");
    } else {
        printf("|--------------------------ͼ�������Ϣ---------------------------|\n");
        printf("|���       ����      ����      ������       ���       ����      |\n");
        printf("|-----------------------------------------------------------------|\n");
        for (int j = 0; j < totally_borrow; j++) {
            printf("|%-9s%-8s%-8s%-10s%-9s%-8.1f|\n",
                   bookgrasp[loans_pos[j]].id, bookgrasp[loans_pos[j]].name, bookgrasp[loans_pos[j]].author,
                   bookgrasp[loans_pos[j]].press, bookgrasp[loans_pos[j]].category, bookgrasp[loans_pos[j]].price);
        }
        if (strcmp(members[i].sex, "male") == 0) {
            printf("%s����,����ǰ���ĵ��鼮����%d����\n", members[i].name, totally_borrow);
        } else if (strcmp(members[i].sex, "female") == 0) {
            printf("%sŮʿ,����ǰ���ĵ��鼮����%d����\n", members[i].name, totally_borrow);
        } else {
            printf("%s,����ǰ���ĵ��鼮����%d����\n", members[i].name, totally_borrow);
        }
    }

    printf("�Ƿ���Ҫ�޸�����?(Y/N): ");
    fflush(stdin);
    choice1 = getchar();
    while (choice1 != 'Y' && choice1 != 'N') {
        choice1 = getchar();
    }
    if (choice1 == 'Y') {
        while (1) {
            printf("������ԭ��������:\n");
            fflush(stdin);
            gets(old_password);
            if (strcmp(old_password, members[i].password) == 0) {
                printf("������ȷ!������������:\n");
                fflush(stdin);
                gets(new_password1);
                printf("���ٴ�����������:\n");
                fflush(stdin);
                gets(new_password2);
                if (strcmp(new_password1, new_password2) == 0) {
                    printf("�����޸ĳɹ�!\n");
                    strcpy(members[i].password, new_password2);

                    p2 = fopen("infomember.txt", "w");
                    for (int j = 0; j < member_number; j++) {
                        fprintf(p2, "%s %s %s %s %s\n", members[j].id, members[j].password,
                                members[j].name, members[j].sex, members[j].phone);
                    }
                    fclose(p2);
                    return 1;
                } else {
                    printf("������������벻һ�£��Ƿ�����޸�����?(Y/N):\n");
                    fflush(stdin);
                    choice2 = getchar();
                    while (choice2 != 'Y' && choice2 != 'N') {
                        choice2 = getchar();
                    }
                    if (choice2 == 'N') {
                        break;
                    }
                }
            } else {
                printf("��������Ƿ���������?(Y/N):");
                fflush(stdin);
                choice2 = getchar();
                while (choice2 != 'Y' && choice2 != 'N') {
                    choice2 = getchar();
                }
                if (choice2 == 'N') {
                    break;
                }
            }
        }
    }
    return 0; /* �ɹ��޸�����󣬷��� 1
                 ��������£����� 0 */
}

 /*���ػ�Աid*/
int check_repeat_id(char id[30])
{
    MEMBERINFO members[200];
    FILE *p2;
    int i;

    member_number = 0;
    p2 = fopen("infomember.txt", "r");
    while (fscanf(p2, "%s %s %s %s %s", members[member_number].id, members[member_number].password,
               members[member_number].name, members[member_number].sex, members[member_number].phone) == 5)
    {
        member_number++;
    }
    fclose(p2);

    for(i = 0;i < member_number;i++) {
        if(strcmp(members[i].id,id) == 0) {
            return 1;
        }
    }
    return 0;
}

/*����ȶԺ��� */ 
int compare_password(char *password)
{
	char input[50]; // �ṩ�㹻������ȷ���ܹ������κ�����
    printf("\t\t\t����������: ");
    gets(input); 
    
    if (strcmp(input, password) == 0) {
        return 1; // ������ȷ
    } else {
        return 0;
    }
}

/*��Աע�ắ��*/
void member_login_up() 
{
    MEMBERINFO member;
    FILE *p2;
    char choice1, choice2;
    while(1) {
        
        system("cls");
        fflush(stdin);

        printf("����������ע���id��: ");
        gets(member.id);

        if(check_repeat_id(member.id)) {
            printf("�������id�ѱ�ʹ��!\n");
        } else {
            printf("��������������: (�벻Ҫ�������ˣ�) ");
            gets(member.password);

            printf("�����������ǳ�: ");
            gets(member.name);
            
            while(1) {
                printf("�����������Ա�: (male/female) ");
                gets(member.sex);
                if(strcmp(member.sex, "male") == 0 || strcmp(member.sex, "female") == 0) {
                    break;
                } else {
                    printf("�Ա�������������������!\n");
                }
            }

            printf("�����������ֻ���: ");
            gets(member.phone);

            printf("�Ƿ񱣴�˴�ע����Ϣ��(Y/N)");
            fflush(stdin);
            choice1 = getchar();
            while (choice1 != 'Y' && choice1 != 'N') {
                choice1 = getchar();
            }
            
            if(choice1 == 'Y') {
                p2 = fopen("infomember.txt", "a");
                fprintf(p2, "%s %s %s %s %s\n", member.id, member.password,
                        member.name, member.sex, member.phone);
                fclose(p2);
                printf("�����˻���ע��ɹ�!\n");
            } else {
                printf("������δע�ᡣ\n");
            }
        }

        printf("�Ƿ�����ע��?(Y/N):");
        fflush(stdin);
        choice2 = getchar();
        while (choice2 != 'Y' && choice2 != 'N') {
            choice2 = getchar();
        }
        
        if(choice2 == 'N') {
            break;
        }
    }
}

/* ��Ա��¼���� */
int member_login_in(char account[20])
{
    FILE *p2;
    MEMBERINFO members[200];
    char choice1, choice2;
    int flag1 = 0; // �����жϵ�¼�Ļ�Ա��Ϣ�Ƿ�ע��
    int i;

    member_number = 0;
    p2 = fopen("infomember.txt", "r");
    while (fscanf(p2, "%s %s %s %s %s\n", members[member_number].id, members[member_number].password,
               members[member_number].name, members[member_number].sex, members[member_number].phone) != EOF)
    {
        member_number++;
    }
    fclose(p2);

    // �����˺��Ƿ����
    for (i = 0; i < member_number; i++) {
        if (strcmp(members[i].id, account) == 0) {
            flag1 = 1;
            break;
        }
    }

    if (flag1) {
        while (1) {
            char password_input[20];
            printf("\t\t\t   ����������: ");
            gets(password_input);
            if (strcmp(members[i].password, password_input) == 0) {
                printf("\n\n\n\t\t\t   �˶���ȷ�����ڽ����Ա����...");
                clock_delay();
                return 1;
            } else {
                printf("\n\n\n\t\t\t   ����������������!\n");
                printf("\t\t\t   ���Ƿ�Ҫ������������(Y/N):");
                fflush(stdin);
                choice1 = getchar();
                while (choice1 != 'Y' && choice1 != 'N') {
                    choice1 = getchar();
                }

                if (choice1 == 'N') {
                    return 0;
                }
            }
        }
    } else {
        printf("\n\n\n\t\t\t  ���˺Ż�δע��, �Ƿ���Ҫע���Ա(Y/N):");
        fflush(stdin);
        choice2 = getchar();
        while (choice2 != 'Y' && choice2 != 'N') {
            choice2 = getchar();
        }

        if (choice2 == 'Y') {
            member_login_up();
            return 2;
        } else {
            return 0;
        }
    }
}



/*�鿴��Ա��Ϣ����*/
void ADMIN_watch_member()
{
    FILE *p2;
    int i;
    MEMBERINFO members[200];

    system("cls");
	fflush(stdin);


    member_number = 0;
    p2 = fopen("infomember.txt", "r");
    while (fscanf(p2, "%s %s %s %s %s\n", members[member_number].id, members[member_number].password,
               members[member_number].name, members[member_number].sex, members[member_number].phone) !=EOF)
    {
        member_number++;
    }
    fclose(p2);

    if(member_number <= 0) {
        printf("û���κλ�Ա��Ϣ!\n");
        
    } else {
        //��ʾ��Ա��Ϣ
        printf("ϵͳע���û���%dλ\n",member_number);
	      printf("\n");
	    printf("|---------------------------������Ϣ-----------------------------------|\n");
	    printf("|����        �Ա�      ID              ����             �ֻ���         |\n");
        for (i = 0; i < member_number; i++) {
            printf("|%-12s%-10s%-16s%-17s%-15s|\n",members[i].name, members[i].sex, members[i].id, members[i].password, members[i].phone);
        }
        printf("|----------------------------------------------------------------------|\n");
    }
    printf("�������������һ����\n");
    getchar();
}

/*�鿴����ͼ�������Ϣ����*/
void display_memberbook()
{
    FILE *p3;
	BOOKLOANS bookgrasp[200];
	int book_loans = 0;
	system("cls");
	
    book_loans = 0;
	p3= fopen("memberbook.txt", "r");
    while (fscanf(p3, "%s %s %s %s %s %lf %s", bookgrasp[book_loans].id, bookgrasp[book_loans].name, bookgrasp[book_loans].author, bookgrasp[book_loans].press,
                bookgrasp[book_loans].category, &bookgrasp[book_loans].price,bookgrasp[book_loans].member_id) != EOF) {
        book_loans++;  //���еĽ�����Ϣ
    }
    fclose(p3);

	if(book_loans <= 0) {
        printf("��ǰû�н�����Ϣ");
    }
	else { 
        printf("��ǰ����%d�鼮�����ġ�",book_loans);
        printf("\n");
        printf("|---------------------------����ͼ����Ϣ-----------------------------------|\n");
        printf("|���  ����        ����      ������          ���    ����    ����ID        |\n");
        printf("|                                                                          |\n");
        for(int i=0;i<book_loans;i++) {
            printf("|%-4s%-10s%-8s%-13s%-6s%-6.1f%-12s|\n",bookgrasp[i].id,
                    bookgrasp[i].name,bookgrasp[i].author,bookgrasp[i].press,
                    bookgrasp[i].category,bookgrasp[i].price,bookgrasp[i].member_id);
        }
            
	} 

	printf("\n\n�������������...");
	fflush(stdin);
	getchar(); 
}


