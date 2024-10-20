//
//  ReginaldKuenstlerTabView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

/**
 Two tabs:
 - your palette
 - image generator.
 */

import SwiftUI

struct ReginaldKuenstlerTabView: View {
    @State var selectedTab: Int = 0
    var body: some View {
        TabView(selection:  $selectedTab) {
            UserPaletteView()
                .tag(0)
                .tabItem {
                    Image(systemName: "paintpalette.fill")
                    Text("Your Palette")
                }
            
            ColourComparisonView()
                .tag(1)
                .tabItem {
                    Image(systemName: "paintpalette.fill")
                    Text("Analyzer")
                }
            
        }
    }
}

#Preview {
    ReginaldKuenstlerTabView()
}
