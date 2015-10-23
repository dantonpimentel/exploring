# Create dict from html table
from bs4 import BeautifulSoup

html = """
<tr>
    <td class="sdj" bl="skdjf"><a href="bla.html">Header1</a></td>
    <td class="sdj" bl="skdjf"><a href="ble.html">Header2</a></td>
    <td class="sdj" bl="skdjf"><a href="bli.html">Header3</a></td>
    <td class="sdj" bl="skdjf"><a href="blo.html">Header4</a></td>
    <td class="sdj" bl="skdjf"><a href="blu.html">Header5</a></td>
</tr>
<tr>
    <td class="sdj" bl="skdjf"><input type="radio" name="df"></td>
    <td class="sdj" bl="skdjf">One</td>
    <td class="sdj" bl="skdjf"><a href="foo.html">kjahkjdsj</a></td>
    <td class="sdj" bl="skdjf">jnklsnd, sd sfnd </td>
    <td class="sdj" bl="skdjf">jkrs gd fg d fg </td>
</tr>
<tr>
    <td class="sdj" bl="skdjf"><input type="radio" name="df" value="b2"></td>
    <td class="sdj" bl="skdjf">Two</td>
    <td class="sdj" bl="skdjf"><a href="foo.html">kjahkjdsj</a></td>
    <td class="sdj" bl="skdjf">jnklsnd, sd sfnd </td>
    <td class="sdj" bl="skdjf">jkrs gd fg d fg </td>
</tr>
<tr>
    <td class="sdj" bl="skdjf"><input type="radio" name="df" value="a1"></td>
    <td class="sdj" bl="skdjf">Three</td>
    <td class="sdj" bl="skdjf"><a href="bar.html">BAR</a></td>
    <td class="sdj" bl="skdjf">another line</td>
    <td class="sdj" bl="skdjf">bli</td>
</tr>
<tr>
    <td class="sdj" bl="skdjf"><input type="radio" name="df" value="c3"></td>
    <td class="sdj" bl="skdjf">Four</td>
    <td class="sdj" bl="skdjf"><a href="xyz.html">XyZ</a></td>
    <td class="sdj" bl="skdjf">Iceland, here I go</td>
    <td class="sdj" bl="skdjf">bla bla bla</td>
</tr>
"""

soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

headers_tr = soup.tr
headers_list = []
for td in [child for child in headers_tr if child.name == 'td']:
    headers_list.append(td.get_text())
soup.tr.extract()

print(headers_list)

rows = []
for tr in soup.find_all('tr'):
    row = {}
    count = 0
    for td in [child for child in tr.children if child.name == 'td']:
        row[headers_list[count]] = td.get_text()
        count += 1
        if count > len(headers_list):
            raise Exception("The row has more columns than expected")
    rows.append(row)

from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2)
pp.pprint(rows)
