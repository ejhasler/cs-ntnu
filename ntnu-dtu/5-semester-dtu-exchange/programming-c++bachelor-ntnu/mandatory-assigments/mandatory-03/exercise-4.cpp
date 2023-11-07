#include <iostream>
#include <string>

using namespace std;

/**
 * Asks the user to enter three different words through standard input (STDIN),
 * combines these words into a sentence, and performs various string operations on it.
 */
int main() {

  cout << "\n\tExercise 4)" << endl;
  cout << "----------------------------------\n\n";

  string word1, word2, word3, sentence;

  // a).

  cout << "You will now enter 3 words:" << endl;

  cout << "\n\tWord 1: ";
  cin >> word1;

  cout << "\tWord 2: ";
  cin >> word2;

  cout << "\tWord 3: ";
  cin >> word3;

  // b).

  // Concatenates the three words into a sentence with spaces and a period at the end.
  sentence = word1 + " " + word2 + " " + word3 + ".";
  cout << "\nThe sentence is: " << sentence << endl;

  // c).

  // Prints the length of each word and the total length of the sentence.
  cout << "\nLength of word 1: " << word1.length();
  cout << "\nLength of word 2: " << word2.length();
  cout << "\nLength of word 3: " << word3.length();
  cout << "\nTotal length of the sentence: " << sentence.length();

  // d).

  // Creates a copy of the sentence for manipulation.
  string sentence2 = sentence;

  // e).

  // Replaces characters 10 to 12 with 'xxx' if the sentence is long enough.
  if (sentence2.length() >= 12) {
    sentence2.replace(10, 3, "xxx");
  } else {
    sentence2 = "The sentence was too short.";
  }

  cout << "\nSentence without changes: " << sentence << endl;
  cout << "Sentence with 'xxx' in place of characters 10-12: " << sentence2 << endl;

  // f).

  // Retrieves and prints the first 5 characters of the original sentence.
  string sentence_start = "The sentence was too short.";

  if (sentence.length() >= 5) {
    sentence_start = sentence.substr(0, 5);
  }

  cout << "The first 5 characters of the sentence: " << sentence_start << endl;

  // g).

  // Checks if the substring 'hallo' exists within the sentence.
  bool found_substring = (sentence.find("hallo") != string::npos);

  cout << boolalpha;
  cout << "\nDoes 'hallo' exist in the sentence: " << found_substring << endl;

  // h).

  // Counts the occurrences of the substring 'er' in the sentence.
  int occurrences = 0;
  string::size_type pos = 0;
  string target = "er";

  while ((pos = sentence.find(target, pos)) != string::npos) {
    occurrences++;
    pos += target.length();
  }

  cout << "Number of occurrences of 'er' in the sentence: " << occurrences << endl;

  return 0;
}
