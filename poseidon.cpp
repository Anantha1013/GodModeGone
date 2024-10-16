
#include<stdio.h>
#include<stdlib.h>
#pragma GCC optimize ("O0")
int main()
{
printf("This is main function \\n");
call_f1();
return 0;
}
int call_f1()
{
int flag=0;
char name[8];
printf("This is function f1 \\n");
printf("Enter name Poseidon: ");
scanf("%s", name);
if(flag==0x77)
{
final_f();
}
else
{
failed_f();
}
return 0;
}
int final_f()
{
printf("Not here!\\n");
return 1;
}
int failed_f()

{
printf("Failed!\\n");
return 1;
}
int system_f()
{
printf("SGVyZSBpcyB5b3VvIgZsYWcgOyk");
printf("Ποσειδώνας")
}