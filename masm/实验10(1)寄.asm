assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    db 'Welcome to masm!',0
datasg ends


stacksg segment
    dd 8 dup(0)        
stacksg ends

codesg segment
main: 
    mov ax,datasg
    mov ds,ax
    mov ax,stacksg
    mov ss,ax
    mov sp,16

    mov dh,8 ;行号
    mov dl,3 ;列号
    mov cl,2 ;颜色
    mov ch,0
    mov si,0 ;字符串的首地址
    call show_str

    mov ax,4c00h
    int 21h

show_str:
    push ax
    push es
    push cx
    push dx
    push bx
    push di
    push si

    mov ax,0b800h
    mov es,ax

    ;计算显存的偏移地址
    push cx ; 保存cx，颜色
    push dx ; 保存dx,行号和列号
    
    mov ax,0
    mov ah,dh
    mov bx,180
    mul bx    ; 行号 * 180

    mov bx,0
    pop bx
    mov bh,0 ; 提出列号
    
    add ax,bx
    add ax,bx ; 行号 * 180 + 列号 * 2

    mov di,ax ; 保存显存的偏移地址到di

    mov bx,0
    pop bx
    mov ah,bh
s:  mov cx,0
    mov cl,ds:[si]
    jcxz ok
    mov al,ds:[si]
    mov es:[di],ax ; 把字符和字符属性放到显存中
    inc si
    add di,2
    loop s

ok: pop si
    pop di
    pop bx
    pop dx
    pop cx
    pop es
    pop ax
    ret
codesg ends
end main