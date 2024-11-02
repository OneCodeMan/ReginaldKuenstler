//
//  Artwork.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import Foundation
import SwiftUI

// MARK: Struct for what user inputs
/**
 Artwork with `image` and `title` only.
 Solely for the user input.
 */
struct ArtworkInput: Hashable {
    var image: UIImage
    var title: String
}

/**
 Artwork with colour pairs.
 */
struct Artwork: Hashable {
    
    static func == (lhs: Artwork, rhs: Artwork) -> Bool {
        lhs.title == rhs.title
    }
    
    var image: UIImage
    var title: String
    var colourPairs: [ColourPair]
    
    init(artworkInput: ArtworkInput, title: String, colourPairs: [ColourPair]) {
        self.image = artworkInput.image
        self.title = title
        self.colourPairs = colourPairs
    }
}
