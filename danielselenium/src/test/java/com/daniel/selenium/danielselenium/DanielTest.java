package com.daniel.selenium.danielselenium;

import static org.junit.Assert.assertEquals;

import java.io.File;
import java.io.IOException;

import org.apache.commons.io.FileUtils;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class DanielTest {
	private String BASE_URL = "http://www.google.com";
	private WebDriver driver;
	private ScreenshotHelper screenshotHelper;

	@Before
	public void openBrowser() {
		System.setProperty("webdriver.chrome.driver","/Users/i055917/Documents/chromedriver");
		driver = new ChromeDriver();
		driver.get(BASE_URL);
		screenshotHelper = new ScreenshotHelper();
	}

	@After
	public void saveScreenshotAndCloseBrowser() throws IOException {
		screenshotHelper.saveScreenshot("screenshot.png");
		driver.quit();
	}

	@Test
	public void pageTitleAfterSearchShouldBeginWithDrupal() throws IOException {
		assertEquals("Google", driver.getTitle());
		WebElement searchField = driver.findElement(By.name("q"));
		searchField.sendKeys("Daniel");
		searchField.submit();
	}

	private class ScreenshotHelper {

		public void saveScreenshot(String screenshotFileName) throws IOException {
			File screenshot = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
			FileUtils.copyFile(screenshot, new File(screenshotFileName));
		}
	}
}
