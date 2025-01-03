;编写0号中断的处理程序

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
    mov ds,ax
    mov si,offset do0

    mov cx,offset do0end - offset do0
    cld 
    rep movsb
    
    mov ax,0000h
    mov ds,ax
    mov word ptr ds:[0*4],0200h
    mov word ptr ds:[0*4+2],0000h
    
    mov ax,4c00h
    int 21h

do0:jmp short do0start
    db "overflow!"
do0start:
    push ax
    push es
    push di
    push si
    push cx

    mov ax,0b800h
    mov es,ax
    mov di,12 * 160 + 36 * 2
    mov ax,cs
    mov ds,ax
    mov si,0202h
    mov cx,9

s:  mov al,ds:[si]
    mov es:[di],al
    add di,2
    inc si
    loop s
    
    pop cx
    pop si
    pop di
    pop es
    pop ax

    mov ax,4c00h
    int 21h
do0end:
    nop
codesg ends
end main