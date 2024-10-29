//
//  CustomFont.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-29.
//

import Foundation
import SwiftUI

extension Font {
    static var defaultFontListItem: Font {
        return Font.custom("Merriweather-Bold", size: 14.0)
    }
    
    static var defaultFontCaption: Font {
        return Font.custom("Merriweather-Bold", size: 16.0)
    }
    
    static var defaultFontButton: Font {
        return Font.custom("Merriweather-Bold", size: 16.0)
    }
    
    static var defaultFontTitle: Font {
        return Font.custom("Merriweather-Bold", size: 20.0)
    }
    
    static var defaultFontLargeTitle: Font {
        return Font.custom("Merriweather-Bold", size: 24.0)
    }
}
