;编程,字符串的输入
;在输入的同时需要显示这个字符串
;一般字输入回车符后，字符串输入结束
;能够删除已经输入的字符串
;用一个子程序实现字符串的入栈，出栈和显示
;
assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    db 16 dup(0)
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

    mov ah,0    ;(ah) = 扫描码
    int 16h     ;(al) = 字符的ASCLL码

getchar:
    cmp al,20h
    jb nochar
    mov ah,0
    call sub1
    mov ah,2
    call sub1
    jmp short getchar

nochar:
    push ax

    cmp al,8    ;退格键的ASCLL码
    je backspace
    cmp al,10
    je enter
    jmp short getchar

backspace:
    mov ah,1
    call sub1
    mov ah,2
    call sub1
    jmp short getchar

enter:
    mov al,0
    mov ah,0
    call sub1
    mov ah,2
    call sub1
    
    pop ax
    ret
sret:
    mov 4c00h
    int 21h

sub1:
    jmp short start1
    top dw 0    ;栈顶
    table dw pushstr,popstr,showstr
start1:
    push ax
    push bx
    push si
    push di
    push cx

    cmp ah,2
    ja subret   ;(ah) = 功能号
    mov bl,ah   ;(al) = 入栈字符/返回的字符
    mov bh,0    ;(dh)、(dl) = 字符在屏幕上显示的位置
    add bx,bx   ;
    mov si,top
    call word ptr table[bx]

pushstr:
    mov ds:[si],al
    inc top
    jmp short subret

popstr:         ;检查是否栈空
    cmp top,0
    je subret
    dec top
    mov si,top
    mov al,ds:[si]
    jmp short subret

showstr:

    mov ax,0b800h
    mov es,ax
    mov ax,160
    mul dh
    mov dl,dh
    mov dh,0
    add dx,dx
    add ax,dx
    mov di,ax

    mov si,0    
    mov cx,top
    cld
    rep movsb

subret:
    pop cx
    pop di
    pop si
    pop bx
    pop ax
    ret

codesg ends
end main
