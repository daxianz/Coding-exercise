;在屏幕的5行12列显示字符串"Welcome to masm!"
;使用第21号中断例程的9号子程序,功能，在光标位置显示字符串
;第10号中断例程的2号子程序,功能,设置光标位置

assume cs:codesg,ds:datasg

datasg segment
    db 'Welcome to masm!','$'    
datasg ends

codesg segment
main: 
    mov ah,2
    mov bh,0
    mov dh,5
    mov dl,12
    int 10h

    mov ah,9
    mov al,0
    mov ax,datasg
    mov ds,ax
    mov dx,0
    int 21h

    mov ax,4c00h
    int 21h

codesg ends
end main