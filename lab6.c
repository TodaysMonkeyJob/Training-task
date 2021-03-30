#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>

int main(int argc, char** argv) {
	int n = 20, data[n];
    srand(time(NULL));
    
	MPI_Status status;
	MPI_Init(&argc, &argv);

	int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);


    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (rank == 0){
		printf("Intial array ");
		for(int i = 0; i<n; ++i) {
        	data[i] = rand()%100;
			printf("%d ",data[i]);
    	}
		printf("\n");
		printf("Send data from %d \n",rank);
		MPI_Send(&data, n, MPI_INT, 1, 1, MPI_COMM_WORLD);
		int recv_data[n];
		MPI_Recv(&recv_data, n, MPI_INT,1,1,MPI_COMM_WORLD, &status);
		printf("Recieved data in %d \n",rank);
		printf("Modified array ");
		for(int i = 0; i<n; ++i) {
			printf("%d ",recv_data[i]);
    	}
	}
	if (rank ==1){
		
		int recv_data[n];
		MPI_Recv(&recv_data, n, MPI_INT,0,1,MPI_COMM_WORLD, &status);
		printf("Recieved data in %d\n",rank);
		for(int i = 0; i<n; ++i) {
			recv_data[i] *= 3;
    	}
		MPI_Send(&recv_data, n, MPI_INT,0,1,MPI_COMM_WORLD);
		printf("Send data from %d \n",rank);

	}


	MPI_Finalize();
    return 0;
}
