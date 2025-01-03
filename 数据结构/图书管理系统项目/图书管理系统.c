#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

/*宏定义区*/ 
#define  ADMIN_password "123456" /*管理员登录密码*/

//书籍信息
typedef struct book 
{
    char id[50];       //编号
    char name[50];    //书名
    char author[50];   //作者
    char press[50];    //出版社
    char category[50]; //分类
    double price;       //价格
} BOOKINFO;
int library_quantity = 0;

//会员借出书籍信息
typedef struct book_loans
{
    char id[50];       //编号
    char name[50];    //书名
    char author[50];   //作者
    char press[50];    //出版社
    char category[50]; //分类
    double price;       //价格
    char member_id[50];//会员编号
} BOOKLOANS;
int book_loans = 0;//总的书籍借阅量

//会员信息
typedef struct member 
{
    char id[50];       //账户
    char password[50]; //密码
    char name[50];     //姓名
    char sex[10];      //性别
    char phone[12];    //手机号
} MEMBERINFO;
int member_number = 0;

/*菜单函数区*/
void menu1();
void menu2();
void menu3();

/*工具函数区*/
int compare_password(char password[20]);/*密码比对函数 */  
void clock_delay(); /*时间延时函数*/ 
void password_circle();/*密码框装饰函数*/
int is_library_empty();/*判断书库中是否有图书信息*/

/*会员信息系统层级函数区*/
int user_account(char account[20]);/*个人账户信息*/ 
void member_login_up();/*会员注册函数*/
int member_login_in(char account[20]);/*会员登录函数*/ 
void ADMIN_watch_member();/*查看会员信息函数*/
void display_memberbook();/*查看所有图书借阅信息函数*/
int check_repeat_id(char id[30]);/*检查账户重复性函数*/ 

/*图书信息系统层级函数区*/
void add_book();/*输入新进的图书信息*/
void delete_book();/*根据图书名称对图书信息进行删除*/
void modify_book();/*修改图书信息*/
void display_book();/*显示全部图书信息*/
void search_book();/*根据图书名称显示图书的信息*/
void borrow_book(char account[20]);/*借书*/
void return_book(char account[20]);/*还书*/
int check_repeat_book(char number[30]);/*查重书籍编号*/

int main()
{
    int flag1=1,flag2=1,flag3=1;/* flag是判断条件,flag为 1 时为真，为 0 时为假 */
	char choice;
	FILE *p1,*p2,*p3;

    system("title 图书管理系统");
    system("color E9");

    if((p1 = fopen("library.txt","r")) == NULL) { 
        p1 = fopen("library.txt","w"); /*p1,书籍信息文件指针*/
        fclose(p1);
    }
    if((p2 = fopen(".txt","r")) == NULL) {
        p2 = fopen("infomember.txt","w"); /*p2,会员个人信息文件指针*/ 
        fclose(p2);
    }
    if((p3 = fopen("memberbook.txt","r")) == NULL) {
        p3 = fopen("memberbook.txt","w"); /*p3,会员借阅书籍信息文件指针*/ 
        fclose(p3);
    }
    while (1)
    {
        system("cls");
		menu1();/*调出主菜单 */ 

  		printf("\n");
        printf("\t\t\t请输入您所要执行的功能(1-4):");
        choice=getchar();
  		while(choice!='1'&&choice!='2'&&choice!='3'&&choice!='4'&&choice!='5') {
            choice=getchar();
        }
  		fflush(stdin);

        if(choice == '1') {
            /*会员功能*/
            int flag=0;
			char account[20],account_choice;
			system("cls");
			password_circle();
            gets(account);
            flag = member_login_in(account); /*登录*/ 
            /*没注册的会调用注册函数*/

            if(flag == 2) { //没注册，注册完了重新登录
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
                    
                    printf("\t\t\t请您选择(1-6):");
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
                                        printf("\n\n登录信息改变,请重新登录...");
                                        clock_delay();
                                        flag3=0;
                                    }
                                break;
                        case '6':
                                printf("\n\n\t\t\t正在退出用户界面...");
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
            /*会员注册*/
            system("cls");
			printf("\n\n\n\t\t\t正在进入用户注册界面...");
			clock_delay();
     	    member_login_up();
        } else if(choice == '3') {
            /*管理员登录*/
            if(compare_password(ADMIN_password)) { 
                printf("\n\n\t\t\t\t  --输入密码正确!--\n\n\t\t\t\t==正在进入管理员界面==\n");
     	  	 	clock_delay(); 
                char manager_choice;
                while(flag2) {
                    system("cls");
                    menu3();
                    printf("\n");

                    printf("\t\t\t请您选择(1-8):");
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
                                printf("\n\n\t\t\t正在退出管理员界面...");
                                clock_delay();
                                break;
                        default:
                            break;
                    }
  				}
            } else {
                printf("\n\n\t\t\t\t  --输入密码错误!--\n");
     		   	clock_delay();
            }
        } else {
            /*退出系统*/
            break;
        }
    }

    fflush(stdin);
	system("cls");
    printf("您已安全地退出系统!\n(按任意键关闭界面)");
    printf("欢迎您的下次使用!\n");
    getchar();
    return 0;
}




/*菜单函数区*/

void menu1()
{
	system("color E9");
	printf("\n\n");
	printf("\t\t\t *=======================================*\n");
	printf("\t\t\t|  * - * - * 图书管理系统 * - * - *  |\n");
	printf("\t\t\t| *                                     * |\n");
	printf("\t\t\t| |  [1]   会员登录                     | |\n");
	printf("\t\t\t| *                                     * |\n");
	printf("\t\t\t| |  [2]   会员注册                     | |\n");
	printf("\t\t\t| *                                     * |\n");
	printf("\t\t\t| |  [3]   管理员登录                   | |\n");
	printf("\t\t\t| *                                     * |\n");
	printf("\t\t\t| |  [4]   退出系统                     | |\n");
	printf("\t\t\t| *                                     * |\n");
	printf("\t\t\t|  * - * - * - * - * - * - * - * - * - *  |\n");
	printf("\t\t\t *=======================================*\n");
}

void menu2()
{
	system("color F9");
	printf("\n\n");
	printf("\t\t\t *=====================================*\n");
    printf("\t\t\t| | * - * - * -会-员-界-面- * - * - * | |\n");
    printf("\t\t\t| *                                   * |\n");
    printf("\t\t\t| |  [1]   查找图书信息               | |\n");
    printf("\t\t\t| *  [2]   借阅图书                   * |\n");
    printf("\t\t\t| |  [3]   归还图书                   | |\n");
    printf("\t\t\t| *  [4]   书库所有图书信息           * |\n");
    printf("\t\t\t| |  [5]   您的账户信息               | |\n");
    printf("\t\t\t| *  [6]   退出用户界面               * |\n");
    printf("\t\t\t| |                                   | |\n");
    printf("\t\t\t| * - * - * - * - * - * - * - * - * - * |\n");
	printf("\t\t\t *=====================================*\n");
}

void menu3()
{
	system("color F9");
	printf("\n\n");
	printf("\t\t\t *======================================*\n");
	printf("\t\t\t| | * - * - * 管-理-员-界-面 * - * - * | |\n");
	printf("\t\t\t| *                                    * |\n");
	printf("\t\t\t| |  [1]   添加图书                    | |\n");
	printf("\t\t\t| *  [2]   删减图书                    * |\n");
	printf("\t\t\t| |  [3]   修改图书信息                | |\n");
	printf("\t\t\t| *  [4]   查找图书信息                * |\n");
	printf("\t\t\t| |  [5]   显示全部图书信息            | |\n");
	printf("\t\t\t| *  [6]   显示所有会员信息            * |\n");
	printf("\t\t\t| |  [7]   显示所有借阅信息            | |\n");
	printf("\t\t\t| *  [8]   退出管理员界面              * |\n");
	printf("\t\t\t| |                                    | |\n");
	printf("\t\t\t| * - * - * - * - * -- * - * - * - * - * |\n");
	printf("\t\t\t *======================================*\n");
}

/*工具函数区*/

/*时间延时函数*/
#include <time.h>

void clock_delay()
{
    clock_t start_time = clock();
    // 1秒 = CLOCKS_PER_SEC个时钟周期
    // 1000毫秒 = CLOCKS_PER_SEC / 1000个时钟周期
    while ((clock() - start_time) < (CLOCKS_PER_SEC / 1000) * 1000);
}


/*密码框装饰函数*/
void password_circle()
{
	system("cls");
	printf("\n\n\n\t\t\t***================================*** \n");
	printf("\t\t\t                                   \n");
	printf("\t\t\t   账户 (account):");
}

/*判断书库中没有任何书籍信息*/
int is_library_empty(int library_quantity)
{
	if(!library_quantity) {
		printf("书库中没有任何书籍信息！\n");
        printf("按任意键返回主菜单。");
        getchar();
		return 1;
	}
	return 0;
}


/*图书信息系统层级函数区*/

//查重书籍编号
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
    char choice1,choice2;//choice1,是否保存添加的书籍,choice2,是否继续添加图书信息
    system("cls");
    /*该书籍已经被添加到书库中*/
    /*成功保存书籍信息*/
    /*没保存书籍信息*/
    while(1) {
        
        fflush(stdin);
        printf("请输入需要添加的书籍编号：");
        gets(newbook.id);

        if(check_repeat_book(newbook.id)) 
        {
            printf("该书籍已经被添加到书库中。\n");
            getchar();
        } else {
            fflush(stdin);
            printf("请输入书名:");
			gets(newbook.name);
		
			printf("请输入作者:");
			gets(newbook.author);
		
			printf("请输入出版社:");
			gets(newbook.press);
			
			printf("请输入类别(文学/科学/理学/工学/等):");
			gets(newbook.category);
		
			printf("请输入价格:");
			scanf("%lf",&newbook.price);

            fflush(stdin);

            printf("是否保存该书籍信息(Y/N):");
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
                printf("已经成功保存新的书籍信息。\n");
            } else {
                printf("未保存该书籍信息。\n");
            }
        }

        printf("是否继续添加图书信息?(Y/N):");
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
    char delete_book[20] = ""; //用来存放要删除的书名
    BOOKINFO books[200];
    FILE *p1;
    char choice1,choice2;
    int i;
    system("cls");

    while (1)
    {
        fflush(stdin);
        printf("请输入要删除的书名:");
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
            printf("书库中没有《%s》的书籍信息。\n",delete_book);
        } else {
            printf("是否删除《%s》的书籍信息?(Y/N):",delete_book);
            choice1 = getchar();
            while (choice1 != 'Y' && choice1 != 'N') {
                choice1 = getchar();
            }
            if(choice1 == 'Y') {
                for(;i < library_quantity;i++) { //越界怎么处理?
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
                printf("已成功删除《%s》的书籍信息。\n",delete_book);
            } else {
                printf("《%s》的书籍信息没有被删除。\n",delete_book);
            }
        }

        printf("是否继续进行删除操作?(Y/N):"); //用户没执行删除操作，没有找到要删除的书籍
        choice2 = getchar();
        while (choice2 != 'Y' && choice2 != 'N') {
            choice2 = getchar();
        }
        if(choice2 == 'N') {
            break;
        }
    }
}

/*修改书籍信息*/
void modify_book()
{
    char id[50];       //编号
    char name[50];     //书名
    char author[50];   //作者
    char press[50];    //出版社
    char category[50]; //分类
    double price;      //价格

    char search_name[30]; //要修改的书名
    char change; //要修改的书籍信息编号
    FILE *p1;
    BOOKINFO books[200];
    char choice1, choice2;
    int i;
    int flag1; // flag1 = 1,没找到要修改的图书信息和正常修改完一本图书信息
    int flag2; // flag2 = 1,要修改的图书信息与馆内信息重复
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
        printf("请输入要修改信息的书籍名: ");
        gets(search_name);

        for (i = 0; i < library_quantity; i++) {
            if (strcmp(books[i].name, search_name) == 0) {
                break;
            }
        }

        if (i >= library_quantity) {
            printf("未找到《%s》的书籍信息。\n", search_name);
            flag1 = 1;
        } else {
            printf("\n"); 
            printf("|---------------------------------图书信息----------------|\n");
            printf("|编号  书名        作者      出版社          类别    单价  |\n");
            printf("|                                                                          |\n");
            printf("|%-6s%-12s%-10s%-16s%-8s%-8.1f|\n",
                books[i].id, books[i].name, books[i].author,
                books[i].press, books[i].category, books[i].price);

            while (1)
            {
                printf("您想修改的书籍信息是?\n");
                printf("1.编号\n2.书名\n3.作者\n4.出版社\n5.类别\n6.单价\n");
                printf("输入选项编号: ");
                change = getchar();
                while (change < '1' || change > '6')
                {
                    change = getchar();
                }
                fflush(stdin);
                printf("请输入新的词条: ");
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
                    printf("您要修改的图书信息与馆内信息重复!\n");
                    break;
                } else {
                    printf("是否继续修改《%s》图书信息?(Y/N):", search_name);
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

        //重新输入要修改的图书信息：1,没找到图书,2,正常修改完一本图书信息,3,要修改的图书信息与管内信息重复
        if (flag1 || flag2) {
            printf("是否继续修改图书信息?(Y/N):");
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

                printf("已经成功保存新的书籍信息。\n");
                break;
            }
        }
    }
}

/*根据图书名称显示图书的信息*/
void search_book()
{
    char search[30] = "";  // 将要查找的字段放到该数组中，可以为id,name,author
    char compare[30] = ""; // 将书库中的字段放到该数组中
    BOOKINFO books[200];
    FILE *p1;
    char choice1, choice2; 
    // choice1,用于选择用什么字段查询
    // choice2,用于是否继续查询
    int flag1; // flag1 = 1，查询的字段是作者,一位作者可以对应多本书的情况
    int flag2; // flag2 = 1，是否查询到符合要求的书籍
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
        printf("您想通过哪种方式查询书籍?\n");
        printf("1.编号\n2.书名\n3.作者\n");
        choice1 = getchar();
        while (choice1 != '1' && choice1 != '2' && choice1 != '3') {
            choice1 = getchar();
        }

        printf("请输入查找的字段信息: ");
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
                printf("|--------------------------图书信息-------------------------|\n");
      			printf("|编号  书名        作者      出版社          类别    单价   |\n");
      			printf("|                                                           |\n");
                printf("|%-6s%-12s%-10s%-15s%-8s%-8.1f|\n",
                       books[i].id, books[i].name, books[i].author,
                       books[i].press, books[i].category, books[i].price);
                flag2 = 1;
                if (!flag1) { // flag1 = 1，查询字段是作者
                    break;
                }
            }
        }

        if (!flag2) {
            printf("没有找到符合您要求的书籍!\n");
        }

        printf("是否继续查询?(Y/N):");
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
        printf("请输入要借的书籍名称:\n");
        fflush(stdin);
        gets(search);

        for(i = 0;i < library_quantity;i++) {
            if(strcmp(books[i].name,search) == 0) {
                break;
            }
        }
            
        if(i >= library_quantity) {
            printf("书库中没有《%s》的书籍信息。\n",search); //是否继续借书
        } else {
            library_quantity--;

            p3=fopen("memberbook.txt","a");
            fprintf(p3,"%s %s %s %s %s %f %s\n",
                    books[i].id,books[i].name,books[i].author,books[i].press,
                    books[i].category,books[i].price,account);
            fclose(p3); 

            printf("借书成功!\n"); /*更新书库*/
        }
        
        printf("您是否继续借书?(Y/N):");
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
    int book_loans = 0;//总的被借的书籍数量
	int member_loans = 0;//该用户借阅书籍数量
    int memberbooks[30]; //用户借阅书籍在bookgrasp中的数组下标

	system("cls");
    fflush(stdin);

    p3= fopen("memberbook.txt", "r");
    while (fscanf(p3, "%s %s %s %s %s %lf %s", bookgrasp[book_loans].id, bookgrasp[book_loans].name, bookgrasp[book_loans].author, bookgrasp[book_loans].press,
                bookgrasp[book_loans].category, &bookgrasp[book_loans].price,bookgrasp[book_loans].member_id) != EOF) {
        book_loans++;  //所有的借书信息
    }
    fclose(p3);

    for(i = 0;i < book_loans;i++) {
        if(strcmp(bookgrasp[member_loans].member_id,account) == 0) {
            memberbooks[member_loans++] = i; //该用户的借书信息
        }
    }

    if(member_loans <= 0) {
        printf("您没有任何借书信息。\n");
        printf("请按任意键返回。\n");
        getchar();  //终止
    } else {
        printf("您所借阅的所有图书信息如下:\n"); 
        printf("|----------------------------图书借阅信息--------------------|\n");
        printf("|编号  书名        作者      出版社          类别    单价    |\n");
        for(i = 0;i < member_loans;i++) {
            int ret = memberbooks[i];
            printf("|%-6s%-12s%-10s%-16s%-8s%-8.1f|\n",bookgrasp[ret].id,
                        bookgrasp[ret].name,bookgrasp[ret].author,bookgrasp[ret].press,
                        bookgrasp[ret].category,bookgrasp[ret].price);
        }
        
        while (1)
        {
            printf("\n输入要归还的书本名:\n");
            gets(search);
            fflush(stdin);

            int j; //用j保存找到的search
            for(j = 0;j < member_loans;j++) {
                int ret = memberbooks[j];
                if(strcmp(bookgrasp[ret].name,search) == 0) { 
                    break;
                }
            }

            if(j >= member_loans) {
                printf("您没有这条借书信息!请核对书名。\n");
            } else {
                book_loans--;
                for(i = memberbooks[j];i < book_loans;i++) {
                    bookgrasp[i] = bookgrasp[i+1];  //数组越界
                }
                member_loans--;
                for(i = j;i < member_loans;i++) {
                    memberbooks[i] = memberbooks[i+1]; //数组越界
                }
                printf("还书成功!\n");
            }

            printf("是否继续还书?(Y/N):");
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

/*显示全部图书信息*/
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

    
    
    printf("\t\t\t书库中共有%d本书。\n", library_quantity);
    printf("|------------------------图书信息-------------------------|\n");
    printf("|编号  书名        作者      出版社          类别    单价  |\n");
    printf("|                                                        |\n");
    for (i = 0; i < library_quantity; i++) {
        printf("|%-6s%-12s%-10s%-16s%-8s%-8.1f|\n",
               books[i].id, books[i].name, books[i].author,
               books[i].press, books[i].category, books[i].price);
    }

    printf("\n按任意键返回上一级。\n");
    getchar();
    fflush(stdin);
}

/*会员信息系统层级*/

/*个人账户信息*/ 
int user_account(char account[20])  
{
    MEMBERINFO members[200];
    BOOKLOANS bookgrasp[200]; //会员借出书籍信息表
    int loans_pos[100]; //用于存放用户借的书在BOOKLOANS books中的数组下标
    int totally_borrow = 0; //用户借书数量计数/借书总量
    char old_password[30];
    char new_password1[30];
    char new_password2[30];
    char choice1; //是否修改密码
    char choice2; //是否继续修改密码
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
        printf("未找到用户信息。\n");
        return 0;
    }

    printf("\n");
    printf("|---------------------------个人信息-----------------------------------|\n");
    printf("|姓名        性别      ID              密码             手机号         |\n");
    printf("|%-12s%-10s%-16s%-17s%-15s|\n",members[i].name, members[i].sex, members[i].id, members[i].password, members[i].phone);
    printf("|                                                                      |\n");
    printf("|----------------------------------------------------------------------|\n");

    for (int j = 0; j < book_loans; j++) {
        if (strcmp(bookgrasp[j].member_id, account) == 0) {
            loans_pos[totally_borrow++] = j;
        }
    }

    if (totally_borrow <= 0) {
        printf("您在图书馆中没有任何借书信息。\n");
    } else {
        printf("|--------------------------图书借阅信息---------------------------|\n");
        printf("|编号       书名      作者      出版社       类别       单价      |\n");
        printf("|-----------------------------------------------------------------|\n");
        for (int j = 0; j < totally_borrow; j++) {
            printf("|%-9s%-8s%-8s%-10s%-9s%-8.1f|\n",
                   bookgrasp[loans_pos[j]].id, bookgrasp[loans_pos[j]].name, bookgrasp[loans_pos[j]].author,
                   bookgrasp[loans_pos[j]].press, bookgrasp[loans_pos[j]].category, bookgrasp[loans_pos[j]].price);
        }
        if (strcmp(members[i].sex, "male") == 0) {
            printf("%s先生,您当前借阅的书籍共有%d本。\n", members[i].name, totally_borrow);
        } else if (strcmp(members[i].sex, "female") == 0) {
            printf("%s女士,您当前借阅的书籍共有%d本。\n", members[i].name, totally_borrow);
        } else {
            printf("%s,您当前借阅的书籍共有%d本。\n", members[i].name, totally_borrow);
        }
    }

    printf("是否需要修改密码?(Y/N): ");
    fflush(stdin);
    choice1 = getchar();
    while (choice1 != 'Y' && choice1 != 'N') {
        choice1 = getchar();
    }
    if (choice1 == 'Y') {
        while (1) {
            printf("请输入原来的密码:\n");
            fflush(stdin);
            gets(old_password);
            if (strcmp(old_password, members[i].password) == 0) {
                printf("密码正确!请输入新密码:\n");
                fflush(stdin);
                gets(new_password1);
                printf("请再次输入新密码:\n");
                fflush(stdin);
                gets(new_password2);
                if (strcmp(new_password1, new_password2) == 0) {
                    printf("密码修改成功!\n");
                    strcpy(members[i].password, new_password2);

                    p2 = fopen("infomember.txt", "w");
                    for (int j = 0; j < member_number; j++) {
                        fprintf(p2, "%s %s %s %s %s\n", members[j].id, members[j].password,
                                members[j].name, members[j].sex, members[j].phone);
                    }
                    fclose(p2);
                    return 1;
                } else {
                    printf("两次输入的密码不一致，是否继续修改密码?(Y/N):\n");
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
                printf("密码错误，是否重新输入?(Y/N):");
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
    return 0; /* 成功修改密码后，返回 1
                 其他情况下，返回 0 */
}

 /*查重会员id*/
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

/*密码比对函数 */ 
int compare_password(char *password)
{
	char input[50]; // 提供足够长度以确保能够储存任何输入
    printf("\t\t\t请输入密码: ");
    gets(input); 
    
    if (strcmp(input, password) == 0) {
        return 1; // 密码正确
    } else {
        return 0;
    }
}

/*会员注册函数*/
void member_login_up() 
{
    MEMBERINFO member;
    FILE *p2;
    char choice1, choice2;
    while(1) {
        
        system("cls");
        fflush(stdin);

        printf("请输入您想注册的id名: ");
        gets(member.id);

        if(check_repeat_id(member.id)) {
            printf("您输入的id已被使用!\n");
        } else {
            printf("请输入您的密码: (请不要告诉他人！) ");
            gets(member.password);

            printf("请输入您的昵称: ");
            gets(member.name);
            
            while(1) {
                printf("请输入您的性别: (male/female) ");
                gets(member.sex);
                if(strcmp(member.sex, "male") == 0 || strcmp(member.sex, "female") == 0) {
                    break;
                } else {
                    printf("性别输入有误，请重新输入!\n");
                }
            }

            printf("请输入您的手机号: ");
            gets(member.phone);

            printf("是否保存此次注册信息？(Y/N)");
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
                printf("您的账户已注册成功!\n");
            } else {
                printf("您本次未注册。\n");
            }
        }

        printf("是否重新注册?(Y/N):");
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

/* 会员登录函数 */
int member_login_in(char account[20])
{
    FILE *p2;
    MEMBERINFO members[200];
    char choice1, choice2;
    int flag1 = 0; // 用于判断登录的会员信息是否注册
    int i;

    member_number = 0;
    p2 = fopen("infomember.txt", "r");
    while (fscanf(p2, "%s %s %s %s %s\n", members[member_number].id, members[member_number].password,
               members[member_number].name, members[member_number].sex, members[member_number].phone) != EOF)
    {
        member_number++;
    }
    fclose(p2);

    // 查找账号是否存在
    for (i = 0; i < member_number; i++) {
        if (strcmp(members[i].id, account) == 0) {
            flag1 = 1;
            break;
        }
    }

    if (flag1) {
        while (1) {
            char password_input[20];
            printf("\t\t\t   请输入密码: ");
            gets(password_input);
            if (strcmp(members[i].password, password_input) == 0) {
                printf("\n\n\n\t\t\t   核对正确！正在进入会员界面...");
                clock_delay();
                return 1;
            } else {
                printf("\n\n\n\t\t\t   您的密码输入有误!\n");
                printf("\t\t\t   您是否要继续输入密码(Y/N):");
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
        printf("\n\n\n\t\t\t  该账号还未注册, 是否需要注册会员(Y/N):");
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



/*查看会员信息函数*/
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
        printf("没有任何会员信息!\n");
        
    } else {
        //显示会员信息
        printf("系统注册用户有%d位\n",member_number);
	      printf("\n");
	    printf("|---------------------------个人信息-----------------------------------|\n");
	    printf("|姓名        性别      ID              密码             手机号         |\n");
        for (i = 0; i < member_number; i++) {
            printf("|%-12s%-10s%-16s%-17s%-15s|\n",members[i].name, members[i].sex, members[i].id, members[i].password, members[i].phone);
        }
        printf("|----------------------------------------------------------------------|\n");
    }
    printf("按任意键返回上一级。\n");
    getchar();
}

/*查看所有图书借阅信息函数*/
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
        book_loans++;  //所有的借书信息
    }
    fclose(p3);

	if(book_loans <= 0) {
        printf("当前没有借阅信息");
    }
	else { 
        printf("当前共有%d书籍被借阅。",book_loans);
        printf("\n");
        printf("|---------------------------借阅图书信息-----------------------------------|\n");
        printf("|编号  书名        作者      出版社          类别    单价    借阅ID        |\n");
        printf("|                                                                          |\n");
        for(int i=0;i<book_loans;i++) {
            printf("|%-4s%-10s%-8s%-13s%-6s%-6.1f%-12s|\n",bookgrasp[i].id,
                    bookgrasp[i].name,bookgrasp[i].author,bookgrasp[i].press,
                    bookgrasp[i].category,bookgrasp[i].price,bookgrasp[i].member_id);
        }
            
	} 

	printf("\n\n输入任意键返回...");
	fflush(stdin);
	getchar(); 
}

