#include "userprog/syscall.h"
#include <stdio.h>
#include <syscall-nr.h>
#include "threads/interrupt.h"
#include "threads/thread.h"
#include "threads/loader.h"
#include "userprog/gdt.h"
#include "threads/flags.h"
#include "intrinsic.h"
#include "../include/filesys/filesys.h"
#include "../include/filesys/file.h"
#include "../include/userprog/process.h"
#include "../include/threads/palloc.h"

typedef int pid_t;

void syscall_entry (void);
void syscall_handler (struct intr_frame *);

void halt (void) NO_RETURN;
void exit (int status) NO_RETURN;
pid_t fork (const char *thread_name, struct intr_frame *f);
int exec (const char *file);
int wait (pid_t);
bool create (const char *file, unsigned initial_size);
bool remove (const char *file);
int open (const char *file);
int filesize (int fd);
int read (int fd, void *buffer, unsigned length);
int write (int fd, const void *buffer, unsigned length);
void seek (int fd, unsigned position);
unsigned tell (int fd);
void close (int fd);
void check_address(const uint64_t *addr);
/* System call.
 *
 * Previously system call services was handled by the interrupt handler
 * (e.g. int 0x80 in linux). However, in x86-64, the manufacturer supplies
 * efficient path for requesting the system call, the `syscall` instruction.
 *
 * The syscall instruction works by reading the values from the the Model
 * Specific Register (MSR). For the details, see the manual. */

#define MSR_STAR 0xc0000081         /* Segment selector msr */
#define MSR_LSTAR 0xc0000082        /* Long mode SYSCALL target */
#define MSR_SYSCALL_MASK 0xc0000084 /* Mask for the eflags */

void
syscall_init (void) {
	write_msr(MSR_STAR, ((uint64_t)SEL_UCSEG - 0x10) << 48  |
			((uint64_t)SEL_KCSEG) << 32);
	write_msr(MSR_LSTAR, (uint64_t) syscall_entry);

	/* The interrupt service rountine should not serve any interrupts
	 * until the syscall_entry swaps the userland stack to the kernel
	 * mode stack. Therefore, we masked the FLAG_FL. */
	write_msr(MSR_SYSCALL_MASK,
			FLAG_IF | FLAG_TF | FLAG_DF | FLAG_IOPL | FLAG_AC | FLAG_NT);
}



/* The main system call interface */
void
syscall_handler (struct intr_frame *f UNUSED) {
	// TODO: Your implementation goes here.
	int sys_num = f->R.rax; // 번호 받아서
	switch (sys_num)
	{
	case SYS_HALT:
		halt();
		break;
	case SYS_EXIT:
		exit(f->R.rdi);
		break;
	case SYS_FORK:
		f->R.rax = fork(f->R.rdi, f);
		break;
	case SYS_EXEC:
		f->R.rax = exec(f->R.rdi);
		break;
	case SYS_WAIT:
		f->R.rax = wait(f->R.rdi);
		break;
	case SYS_CREATE:
		f->R.rax = create(f->R.rdi, f->R.rsi);
		break;
	case SYS_REMOVE:
		f->R.rax = remove(f->R.rdi);
		break;
	case SYS_OPEN:
		f->R.rax = open(f->R.rdi);
		break;
	case SYS_FILESIZE:
		f->R.rax = filesize(f->R.rdi);
		break;
	case SYS_READ:
		f->R.rax = read(f->R.rdi, f->R.rsi, f->R.rdx);
		break;
	case SYS_WRITE:
		f->R.rax = write(f->R.rdi, f->R.rsi, f->R.rdx);
		break;
	case SYS_SEEK:
		/* code */
		break;
	case SYS_TELL:
		/* code */
		break;
	case SYS_CLOSE:
		/* code */
		break;
	
	default:
		break;
	}
	// printf ("system call!\n");
	// thread_exit ();

}

void halt (void) {
	power_off();
	/*안녕하세요*/
}; // 0

void exit (int status) {
	
	struct thread *cur = thread_current();
	cur->p_status = status;
	printf("%s: exit(%d)\n", cur->name, cur->p_status);
	thread_exit();

	return status;
}; // 1

pid_t fork (const char *thread_name, struct intr_frame *f)
{	
	struct thread *cur = thread_current();
	return process_fork(thread_name, f);
} // 2

int exec (const char *file)
{
	check_address(file); // file_name 포인터가 유효한지 확인합니다.

    char *file_name_copy = palloc_get_page(PAL_ZERO); // 페이지 할당을 통해 파일 이름을 복사할 메모리 공간을 얻습니다.
    if (file_name_copy == NULL)
        exit(-1); // 메모리 할당에 실패한 경우, -1을 반환하고 현재 프로세스를 종료합니다.

    strlcpy(file_name_copy, file, PGSIZE); // file_name을 file_name_copy로 복사합니다. PGSIZE는 복사할 최대 크기를 나타냅니다.

    if (process_exec(file_name_copy) == -1)
        exit(-1);
} // 3

int wait (pid)
	{	
		// printf("하이");
		return process_wait(pid);
	} // 4

bool create (const char *file, unsigned initial_size)
{
	check_address(file);
	// if (file == NULL) return 0;
	
	return filesys_create(file, initial_size);
} // 5

bool remove (const char *file)
{
	if (file == NULL) return 0;
	
	return filesys_remove(file);
} // 6

int open (const char *file)
{

	// printf("%s", file);
	check_address(file);
	
	struct file *open_file = filesys_open(file);
	// printf("%d",open_file); // 0임

	// printf("%s 1234", file);
	if (open_file == NULL) return -1;
	// printf("%s 456", file);
	int fd = to_fd_table(open_file);
	// printf("%s 789 %d", file, fd);
	if (fd == -1)
	{
		file_close(open_file);
	}

	return fd;
} // 7

int filesize (int fd)
{	
	if (fd<0 || fd >= FDCOUNT_LIMIT) return -1;
	struct thread *cur = thread_current();
	struct file *open_file = cur->fd_table[fd];
	return file_length(open_file);
} // 8

int read (int fd, void *buffer, unsigned length)
{

	check_address(buffer);
	

	struct thread *cur = thread_current();
	struct lock lock;
	lock_init(&lock);

	struct file *open_file = cur->fd_table[fd];
	
	
	// 아직 필드 디스크립터 초기화랑 012 설정 안해줌! <- 얼추 함
	if (fd == 0)
	{	
		*(char*)buffer = input_getc();
	}	
	else
	{
		if (fd < 2 || fd > 10) return -1;
		if (open_file == NULL) return -1; 
		lock_acquire(&lock); // ????

		// 예외 필요함

		length = file_read(open_file,buffer,length);
		lock_release(&lock);// ????
		
	}

	return length;

} // 9

int write (int fd, const void *buffer, unsigned length)
{	


	check_address(buffer);
	

	struct thread *cur = thread_current();
	struct file *open_file = cur->fd_table[fd];

	if (fd == 1)
	{
		putbuf(buffer, length);
	}
	else
	{	
		if (fd < 2 || fd > 10) return -1;
		if (open_file == NULL) return -1;
		length = file_write(open_file, buffer, length);
	}

	return length;

} // 10

void seek (int fd, unsigned position); // 11
unsigned tell (int fd); // 12
void close (int fd); // 13


void check_address(const uint64_t *addr)	
{
	// printf("%s",addr);
	struct thread *cur = thread_current();

	// printf("%s", addr);

	if (addr == NULL || !(is_user_vaddr(addr)) || pml4_get_page(cur->pml4, addr) == NULL) {
		// printf("여긴가?");
		exit(-1);
	}
}

int to_fd_table(struct file *file)
{	
	struct thread *cur = thread_current();
	struct file ** fd_table = cur->fd_table;

	// printf();

	while (cur->fd_index < FDCOUNT_LIMIT && fd_table[cur->fd_index])
	{	
		
		cur->fd_index++;
	}
	
	// printf(" %d safasfasfsf %d ", cur->fd_index, FDCOUNT_LIMIT);

	if (cur->fd_index >= FDCOUNT_LIMIT) return -1;

	fd_table[cur->fd_index] = file;

	return cur->fd_index;
}