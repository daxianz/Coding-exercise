;编写子程序,以十六进制的形式在屏幕中间显示给定的字节型数据
;该字节型数据放在ah中

assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    table db '0123456789ABCDEF'
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

    mov ah,11111110b
    call showbyte

    mov ax,4c00h
    int 21h

showbyte:
    push ax
    push cx
    push es
    push si

    mov al,ah
    shr ah,1
    shr ah,1
    shr ah,1
    shr ah,1                ;高四位
    and al,00001111b        ;低四位

    mov cx,0b800h
    mov es,cx
    mov si,12*160 + 39*2

    mov bh,ah
    mov bl,0                ;用高四位作为table的偏移地址
    mov bh,table[bx]        ;取得对应字符
    mov byte ptr es:[si],bh

    mov bl,al
    mov bh,0
    mov bl,table[bx]
    mov byte ptr es:[si+2],bl

    pop si
    pop es
    pop cx
    pop ax
    ret
codesg ends
end main
