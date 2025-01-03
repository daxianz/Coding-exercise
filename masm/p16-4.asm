;编写子程序setscreen,为显示输出提供如下功能
;(1) 清屏
;(2) 设置前景色
;(3) 设置背景色
;(4) 向上滚动一行
;   入口参数说明:
;(1)用ah寄存器传递功能号:0->清屏,1->设置前景色，，，
;(2)对于1,2号功能，用al传送颜色值

assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    
datasg ends

stacksg segment
    dw 16 dup(0)
stacksg ends

codesg segment
main:
    mov ax,stacksg
    mov ss,ax
    mov sp,32
    mov ax,datasg
    mov ds,ax

    mov ah,0
    mov al,0

    

    mov ax,4c00h
    int 21h

setscreen:
    jmp short start

    table dw sub1,sub2,sub3,sub4

start:
    push bx
    cmp ah,3    ;判断功能号是否大于3
    ja sret
    mov bl,ah
    mov bh,0
    call word ptr table[bx]

sret:   
    pop bx
    ret
    
sub1:
    push ax
    push es
    push di
    push cx

    mov ax,0b800h
    mov es,ax
    mov di,0
    mov cx,25 * 80

s1: mov byte ptr es:[di],' '
    add di,2
    loop s1

    pop cx
    pop di
    pop es
    pop ax
    ret

sub2:
    push ax
    push es
    push di
    push cx

    mov ax,0b800h
    mov es,ax
    mov di,1
    mov cx,25 * 80

s2: and byte ptr es:[di],11111000b
    add byte ptr es:[di],al
    add di,2
    loop s2

    pop cx
    pop di
    pop es
    pop ax
    ret

sub3:
    push ax
    push es
    push di
    push cx

    mov cx,4
    shl al,cl

    mov ax,0b800h
    mov es,ax
    mov di,1
    mov cx,25 * 80

s3: and byte ptr es:[di],10001111b
    or es:[di],al
    add di,2
    loop s3

    pop cx
    pop di
    pop es
    pop ax
    ret

sub4:
    push ax
    push es
    push di
    push si
    push cx

    mov ax,0b800h
    mov es,ax
    mov di,0
    mov ds,ax
    mov si,80
    mov cx,24 * 80
    cli
    rep movsw
    
    mov cx,80
s4: mov byte ptr es:[di],' '
    add di,2
    loop s4

    pop cx
    pop si
    pop di
    pop es
    pop ax
    ret
codesg ends
end main
