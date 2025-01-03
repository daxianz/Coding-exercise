
assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    
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

    mov ax,4240h ; 低八位
    mov dx,000fh ; 高八位
    mov cx,0ah
    call divdw

    mov ax,4c00h
    int 21h
divdw:
    mov ds:[0],ax
    mov bx,0ffffh

    mov ax,dx
    mov dx,0
    div cx
    
    mov ds:[2],ax ;把int(H/N)存储

    mov ax,0 ; 计算[rem(H/N)*65536+L]/N
    mul bx
    add ax,ds:[0]
    div cx
    
    mov ds:[4],ax
    mov ax,ds:[2] ; 计算int(H/N)*65536
    mov dx,0
    mul bx

    add ax,ds:[4]
    
    ret
codesg ends
end main