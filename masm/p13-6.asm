
assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    
datasg ends

stacksg segment
    dd 8 dup(0)       
stacksg ends

codesg segment
main: 
    mov ax,stacksg
    mov ss,ax
    mov sp,32
    mov ax,datasg
    mov ds,ax
    mov si,0

    mov ah,2  ;第二个子程序
    mov bh,0  ;第0页
    mov dh,12 ;第11行
    mov dl,36 ;第35列
    int 10h

    mov ah,9  ;第九个子程序
    mov al,'a';字符
    mov bl,7  ;颜色属性
    mov bh,0  ;第0页
    mov cx,5  ;重复次数
    int 10h

    mov ax,4c00h
    int 21h

codesg ends
end main