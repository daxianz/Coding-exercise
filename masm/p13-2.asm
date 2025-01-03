;编写安装中断7ch的中断例程
;该例程求word型数据的平方

assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    db 8 dup(0)
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

    mov ax,0000h
    mov es,ax
    mov di,0200h
    mov ax,cs
    mov ds,ax     ;安装
    mov si,offset do7ch
    mov cx,offset do7chend - offset do7ch
    cld
    rep movsb
    
    mov ax,0000h
    mov ds,ax
    mov [7ch*4],0200h  ;设置中断向量表
    mov [7ch*4+2],0000h

    int 7ch
    mov ax,3456
    add ax,ax
    adc dx,dx

    mov ax,4c00h
    int 21h

do7ch:
    push ax
    push bx
    push dx

    mov bx,ax
    mul bx

    pop dx
    pop bx
    pop ax
    iret
do7chend:
    nop
codesg ends
end main