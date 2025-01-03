;计算datasg段中第一组数据的3次方，结果保留在后面一组dword单元中

assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    dw 1,2,3,4,5,6,7,8
    dd 0,0,0,0,0,0,0,0
datasg ends

stacksg segment 
    dw 8 dup(0)
stacksg ends

codesg segment
main:
    mov ax,datasg
    mov ds,ax
    mov ax,stacksg
    mov ss,ax
    mov sp,16

    mov bx,0
    mov si,16
    mov cx,8
s:
    call cube
    add bx,2
    add si,4
    loop s
    mov ax,4c00h
    int 21h
    
cube:
    push cx

    mov ax,[bx]
    mul word ptr ds:[bx]
    mul word ptr ds:[bx]
    mov [bx+si],ax
    mov [bx+si+2],dx
    
    pop cx
    ret
codesg ends
end main