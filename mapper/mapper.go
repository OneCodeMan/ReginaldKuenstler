package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"sort"

	// importing Colly
	"github.com/gocolly/colly"
)

// initialize a data structure to keep the scraped data
type VColour struct {
	Name, HexCode, RgbValue string
}

func main() {
	var vcolours []VColour

	fmt.Println("Hello, Worssld!")
	targetUrl := "https://htmlcolorcodes.com/"

	c := colly.NewCollector(
		// without all these domains, it won't work.
		colly.AllowedDomains(
			targetUrl,
			"htmlcolorcodes.com/",
			"htmlcolorcodes.com",
			"https://htmlcolorcodes.com",
		),
	)

	c.OnHTML("tr.color-table__row", func(e *colly.HTMLElement) {

		// colour
		colour := VColour{}

		// scrape data
		// extract colour name
		colourName := e.ChildText("td.color-table__cell--name a")
		fmt.Println("Colour name: ", colourName)

		// extract colour hex code
		colourHex := e.ChildText("td.color-table__cell--hex")
		fmt.Println("Colour hex: ", colourHex)

		fmt.Println("\n")

		// assign to colours
		if colourName != "" {
			colour.Name = colourName
			colour.HexCode = colourHex
		}

		// append colour to map
		vcolours = append(vcolours, colour)
	})

	// colly callbacks

	// on visit
	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting: ", r.URL)
	})

	// triggered when the scraper encounters an error
	c.OnError(func(_ *colly.Response, err error) {
		fmt.Println("Something went wrong: ", err)
	})

	// triggered once scraping is done (e.g., write the data to a CSV file)
	c.OnScraped(func(r *colly.Response) {

		// reassurance
		fmt.Println(r.Request.URL, " scraped!")
		fmt.Println("VColours has elements: ", len(vcolours))

		// sort vcolours array alphabetically
		sort.Slice(vcolours, func(i, j int) bool {
			return vcolours[i].Name < vcolours[j].Name
		})

		// remove duplicates
		// Filter the slice, only keeping unique names
		seen := make(map[string]bool)
		vcoloursSanitized := []VColour{}

		for _, c := range vcolours {
			if !seen[c.Name] && c.Name != "" {
				vcoloursSanitized = append(vcoloursSanitized, c)
				seen[c.Name] = true
			}
		}

		fmt.Println("VColoursSanitized has elements: ", len(vcoloursSanitized))

		// csv logic
		// open the CSV file
		file, err := os.Create("colourmap.csv")
		if err != nil {
			log.Fatalln("Failed to create output CSV file", err)
		}
		defer file.Close()

		// initialize a file writer
		writer := csv.NewWriter(file)

		// write the CSV headers
		headers := []string{
			"Name",
			"HexCode",
		}
		writer.Write(headers)

		// write each product as a CSV row
		for _, colour := range vcoloursSanitized {
			// convert a Product to an array of strings
			record := []string{
				colour.Name,
				colour.HexCode,
			}

			// add a CSV record to the output file
			writer.Write(record)
		}
		defer writer.Flush()
	})

	c.Visit("https://htmlcolorcodes.com/colors/")
}
