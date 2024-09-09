#include "userprog/syscall.h"
#include <stdio.h>
#include <syscall-nr.h>
#include "threads/interrupt.h"
#include "threads/thread.h"
#include "threads/loader.h"
#include "userprog/gdt.h"
#include "threads/flags.h"
#include "intrinsic.h"

void syscall_entry (void);
void syscall_handler (struct intr_frame *);

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
	// switch (sys_num)
	// {
	// case SYS_HALT:
	// 	halt();
	// 	break;
	// case SYS_EXIT:
	// 	exit(f->R.rdi);
	// 	break;
	// case SYS_FORK:
	// 	/* code */
	// 	break;
	// case SYS_EXEC:
	// 	/* code */
	// 	break;
	// case SYS_WAIT:
	// 	/* code */
	// 	break;
	// case SYS_CREATE:
		
	// 	break;
	// case SYS_REMOVE:
	// 	/* code */
	// 	break;
	// case SYS_OPEN:
	// 	/* code */
	// 	break;
	// case SYS_FILESIZE:
	// 	/* code */
	// 	break;
	// case SYS_READ:
	// 	/* code */
	// 	break;
	// case SYS_WRITE:
	// 	/* code */
	// 	break;
	// case SYS_SEEK:
	// 	/* code */
	// 	break;
	// case SYS_TELL:
	// 	/* code */
	// 	break;
	// case SYS_CLOSE:
	// 	/* code */
	// 	break;
	
	// default:
	// 	break;
	// }


	printf ("system call!\n");
	thread_exit ();

}

// void halt (void) {
// 	power_off();
// }; // 0

// void exit (int status) {

// 	thread_exit();

// 	return status;
// }; // 1

// pid_t fork (const char *thread_name)
// {	
	
// } // 2

// int exec (const char *file); // 3
// int wait (pid_t); // 4
// bool create (const char *file, unsigned initial_size)
// {

// } // 5
// bool remove (const char *file)
// {

// } // 6
// int open (const char *file); // 7
// int filesize (int fd); // 8
// int read (int fd, void *buffer, unsigned length); // 9
// int write (int fd, const void *buffer, unsigned length); // 10
// void seek (int fd, unsigned position); // 11
// unsigned tell (int fd); // 12
// void close (int fd); // 13
