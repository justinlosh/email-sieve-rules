

# Email Sieve Rules
This repository provides a collection of public domain names and known email addresses used by various websites for communicating with end users. It is specifically designed to help in the creation of **sieve mail filtering rules** and similar tasks related to email security and filtering. The data is organized into various CSV and JSON files for easy integration into mail filtering systems.

## Files

The repository includes the following types of data files:

### CSV Files

* **domain-list.csv**: A list of common domain names associated with popular websites. This can be used to identify incoming emails from specific sources.
* **email-address-list.csv**: A list of known email addresses used by various websites for end-user communications. It can be used to help filter or sort emails from these addresses.

### JSON Files

* **domain-tld.json**: This file contains the domain names and known email addresses specifically for an entities communication systems. More websites will be added to this structure over time.

### File Structure

* `data/domains/domain.tld`

  * `domain-list.csv`
  * `email-address-list.csv`
  * `domain-tld.json`

## Purpose

The goal of this repository is to provide easily accessible, structured data for those working on email filtering, especially for projects like Sieve mail filters, spam prevention, and email categorization systems.

**Note:** This project is intended to provide a helpful dataset for email security solutions and is not affiliated with any of the companies or websites listed.

## How to Use

1. **Download the data**: Clone the repository or download the individual files.
2. **Integrate with your system**: Use the `domains.csv` and `emails.csv` files as part of your mail filtering rules. The JSON files are structured to be easily parsed and expanded for additional website-specific filtering.
3. **Expand the dataset**: If you wish to add more websites, please follow the format in the existing JSON files.

## Legal Disclaimer

This repository and its contents are provided "as is" for educational and informational purposes only. By using this repository, you agree to the following:

1. **No endorsement or affiliation**: This repository is not endorsed by, affiliated with, or in any way connected to the companies or websites listed in the data files. The domain names and email addresses included are publicly available and are used only for the purpose of supporting mail filtering systems.
2. **Use at your own risk**: The data in this repository is made available for non-commercial use only, and it is the responsibility of the user to verify and ensure that it is used in compliance with applicable laws, including but not limited to data protection and privacy regulations.
3. **No warranty**: The data provided in this repository is not guaranteed to be accurate, complete, or up-to-date. The repository owner makes no warranties regarding the suitability or fitness of the data for any particular use.
4. **Prohibited use**: The data is not intended for use in spamming, phishing, or any other malicious activities. The owner of this repository disclaims any responsibility for any misuse of the data.
5. **Modification and Redistribution**: You are free to fork, modify, and redistribute the data under the terms of the MIT License. However, if you do so, you must ensure that your modifications comply with all applicable laws and do not violate the intellectual property rights of third parties.

## License

[ PLACEHOLDER ]

## Contributing

[ PLACEHOLDER ]

## Contact

[ PLACEHOLDER ]

---

### Additional Notes

* **Legal Disclaimer**: The disclaimer ensures that you clarify the limitations and responsibility. It makes it clear that you're not endorsing or affiliated with these companies, and it protects you from any potential legal action for data misuse or inaccuracies.

* **Use at your own risk**: Since this is for filtering purposes, make sure the data isn’t being used for anything malicious, and that users are aware of this restriction.

* **License**: The MIT license is a common open-source license that allows others to freely use, modify, and distribute your code, but it also includes a disclaimer of liability.