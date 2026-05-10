# SGPB 雙拼
基於 Rime 中州韻輸入法引擎，依賴於 [`rime-cantonese`](https://github.com/rime/rime-cantonese)，採用[香港語言學學會粵語拼音方案](https://www.lshk.org/jyutping)。
## 簡介
**SGPB 雙拼**係一種粵語拼音編碼方案，擁有**淸楚易記嘅按鍵位置**。  
![](README/gw.png)
![](README/ai.png)
![](README/am.png)
![](README/oe.png)
## 鍵位圖
採用 QWERTY 佈局
<h3>SGPB 雙拼</h3>
<ul><li>配方：℞ <code>sgpb</code></li></ul>
<table>
	<tr valign="top">
		<td><b>1</b></td>
		<td><b>2</b></td>
		<td><b>3</b></td>
		<td><b>4</b></td>
		<td><b>5</b></td>
		<td><b>6</b></td>
		<td><b>7</b></td>
		<td><b>8</b></td>
		<td><b>9</b></td>
		<td><b>0</b></td>
	</tr>
	<tr valign="top">
		<td><b>Q</b><br/>aau</td>
		<td><b>W</b><br/>aai</td>
		<td><b>E</b></td>
		<td><b>R</b><br/>gw<br/>yut<br/>yun<br/>ut<br/>un</td>
		<td><b>T</b><br/>eot<br/>eon<br/>ot<br/>on</td>
		<td><b>Y</b><br/>yu<br/>jyu<br/>oe</td>
		<td><b>U</b><br/>ou</td>
		<td><b>I</b><br/>kw<br/>ei<br/>ji</td>
		<td><b>O</b></td>
		<td><b>P</b><br/>oi</td>
	</tr>
	<tr valign="top">
		<td><b>A</b><br/>aa</td>
		<td><b>S</b><br/>at<br/>an</td>
		<td><b>D</b><br/>au</td>
		<td><b>F</b><br/>ai</td>
		<td><b>G</b><br/>oek<br/>oeng</td>
		<td><b>H</b><br/>it<br/>in<br/>jit<br/>jin</td>
		<td><b>J</b><br/>eoi<br/>ui</td>
		<td><b>K</b><br/>iu<br/>jiu</td>
		<td><b>L</b><br/>ip<br/>im</td>
		<td><b>;</b></td>
	</tr>
	<tr valign="top">
		<td><b>Z</b><br/>aat<br/>aan</td>
		<td><b>X</b><br/>aap<br/>aam</td>
		<td><b>C</b><br/>aak<br/>aang<br/>ak<br/>ang</td>
		<td><b>V</b><br/>ng<br/>ap<br/>am</td>
		<td><b>B</b><br/>ek<br/>eng<br/>ik<br/>ing<br/>jeng<br/>jik<br/>jing</td>
		<td><b>N</b><br/>uk<br/>ung</td>
		<td><b>M</b><br/>ok<br/>ong</td>
		<td><b>,</b></td>
		<td><b>.</b></td>
		<td><b>/</b></td>
	</tr>
</table>
<details>
	<summary><h3>其他方案</h3></summary>
	<h3>SQMPIV 三拼</h3>
	<ul><li>配方：℞ <code>sqmpiv</code></li></ul>
	<table>
		<tr valign="top">
			<td><b>1</b></td>
			<td><b>2</b></td>
			<td><b>3</b></td>
			<td><b>4</b></td>
			<td><b>5</b></td>
			<td><b>6</b></td>
			<td><b>7</b></td>
			<td><b>8</b></td>
			<td><b>9</b></td>
			<td><b>0</b></td>
		</tr>
		<tr valign="top">
			<td><b>Q</b><br/>aa</td>
			<td><b>W</b></td>
			<td><b>E</b></td>
			<td><b>R</b><br/>gw<br/>eo<br/>oe</td>
			<td><b>T</b></td>
			<td><b>Y</b><br/>kw<br/>yu</td>
			<td><b>U</b></td>
			<td><b>I</b></td>
			<td><b>O</b></td>
			<td><b>P</b></td>
		</tr>
		<tr valign="top">
			<td><b>A</b></td>
			<td><b>S</b></td>
			<td><b>D</b></td>
			<td><b>F</b></td>
			<td><b>G</b></td>
			<td><b>H</b></td>
			<td><b>J</b></td>
			<td><b>K</b></td>
			<td><b>L</b></td>
			<td><b>;</b></td>
		</tr>
		<tr valign="top">
			<td><b>Z</b></td>
			<td><b>X</b></td>
			<td><b>C</b></td>
			<td><b>V</b><br/>ng</td>
			<td><b>B</b></td>
			<td><b>N</b></td>
			<td><b>M</b></td>
			<td><b>,</b></td>
			<td><b>.</b></td>
			<td><b>/</b></td>
		</tr>
	</table>
</details>

## 使用說明
### 聲調輸入
* 配方：℞ `sg1pb3`  
爲咗區分入聲字同非入聲字，可以撳 <kbd>1</kbd> ‒ <kbd>9</kbd> 嚟用聲調篩選。
### 注意
- 對於拼音 `gu`、`gui`、`gun`、`ku`、`kui`、`kut`，聲母要串成 `gw`、`kw`。<details>
	<summary>即係話，</summary>
	如果要打個「古」字，應該撳 <kbd>R</kbd><kbd>U</kbd> 而唔係 <kbd>G</kbd><kbd>U</kbd>。
	<h4>所有情況</h4>
	<table>
		<tr valign="top">
			<th>聲＼韻</th>
			<th><kbd>U</kbd></th>
			<th><kbd>R</kbd></th>
			<th><kbd>T</kbd></th>
		</tr>
		<tr valign="top">
			<th><kbd>G</kbd></th>
			<td><code>gou</code></td>
			<td><code>gyut</code><br/><code>gyun</code></td>
			<td><code>geoi</code></td>
		</tr>
		<tr valign="top">
			<th><kbd>R</kbd></th>
			<td><code>gu</code></td>
			<td><code>gun</code></td>
			<td><code>gui</code></td>
		</tr>
		<tr valign="top">
			<th><kbd>K</kbd></th>
			<td></td>
			<td><code>kyut</code><br/><code>kyun</code></td>
			<td><code>keoi</code></td>
		</tr>
		<tr valign="top">
			<th><kbd>Y</kbd></th>
			<td><code>ku</code></td>
			<td><code>kut</code></td>
			<td><code>kui</code></td>
		</tr>
	</table>
</details>

### 未聽講過雙拼？
**雙拼**係拼音輸入法嘅一種編碼方案。用雙拼打字嘅時候只需要分別撳一下聲母同韻母總共兩個掣就可以打出任意一個漢字。詳見[維基百科](https://zh.wikipedia.org/wiki/%E5%8F%8C%E6%8B%BC)。
### 示例
| 例句 | 廣東人講廣東話，唔識尊重返鄉下。 |
|:---|:---|
| 粵拼全拼 | `gwongdungjangonggwongdungwaa，msikzyunzungfaanhoenghaa。` |
| SGPB 雙拼 | `rmdnjsgmrmdnwa，msbzrznfzhgha。` |
