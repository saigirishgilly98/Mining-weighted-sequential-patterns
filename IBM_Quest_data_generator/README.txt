IBM Synthetic Data Generation Code for Associations and Sequential Patterns

http://www.almaden.ibm.com/software/projects/hdb/resources.shtml

Sequential Pattern Readme file composed by Hong Cheng

Usage: 

	bin/seq_data_generator seq -help			For more detailed list of options
	bin/seq_data_generator seq [options]
	
	"seq" means sequential patterns 
	
Output Format: 
   There are two possible output formats for the data file, based on whether 
   or not the "-ascii" option is specified. 
   * Binary
     The file is in the binary format. The items in an itemset are displayed in increasing 
     order, then followed by a -1, which is         the itemset delimiter. When all the 
     itemsets in a sequence are output, follows a -2 as the sequence delimiter. Then starts 
     a new sequence.

   * Ascii 
     Each line contains a sequence. The first number is the total number of itemsets in this
     sequence. After that, each itemset is displayed, first by the number of items in this 
     itemset, then followed by the items in that itemset, in increasing order.

   Apart from the data file, this program also generates a pattern file. The pattern file 
   has three parts: 
   * A description of the data, including total number of sequences, average sequence length
     and other statistics. 
   * Statistic information about large itemset patterns.
   * Statistic information about large sequential patterns.


Command Line Options:
  -ncust number_of_customers_in_000s (default: 100)
  -slen avg_trans_per_customer (default: 10)
  -tlen avg_items_per_transaction (default: 2.5)
  -nitems number_of_different_items_in_000s (default: 10)
  -rept repetition-level (default: 0)

  -seq.npats number_of_seq_patterns (default: 5000)
  -seq.patlen avg_length_of_maximal_pattern (default: 4)
  -seq.corr correlation_between_patterns (default: 0.25)
  -seq.conf avg_confidence_in_a_rule (default: 0.75)

  -fname <filename> (write to filename.data and filename.pat)
  -ascii (Write data in ASCII format; default: binary)
  -version (to print out version info)


Example:
An example of sequence dataset with 10 sequences

Command:  bin/seq_data_generator seq -ncust 0.01  -ascii -fname sample

9 1 2479 2 2154 5477 4 440 2276 6036 9838 4 6639 7926 9054 9748 1 1247 1 1992 1 2535 3 5095 7744 9337 6 2343 4737 7188 8518 9241 9486 
9 3 765 1542 7203 3 5854 7309 8827 1 5993 4 991 4956 6376 7993 3 606 1798 8964 3 606 1091 2787 2 4023 5242 3 2451 6392 8259 5 703 3355 5892 7169 9239 
6 1 9033 3 1845 7713 8778 3 1285 1705 7890 3 4049 6908 7443 2 765 1739 2 3627 9693 
1 2 269 4701 
2 2 6273 7655 1 2654 
6 1 149 2 3533 9471 1 5758 1 1491 1 5024 1 3812 
8 3 3404 4764 6487 3 5210 7637 7771 3 1405 5501 9708 3 3572 3875 7705 3 2709 4167 5713 7 886 2870 6918 7963 8571 9125 9795 2 723 6970 2 625 5975 
4 1 7851 1 2053 2 5826 8595 1 1734 
6 2 7213 7771 1 5510 2 4652 9373 1 9928 2 6771 7774 2 3113 8769 
5 2 765 6075 1 5735 1 3541 1 2715 1 2104 
