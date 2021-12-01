int main(int argc, char*argv[])
{
	char buf[10];
	int i;
	for (i=0; i<10; i++)
		buf[i] = '-';
	buf[9] = 0;
	snprintf(buf, 10, "%d", 798);
	printf("%s\n", buf);
	return 0;
}
