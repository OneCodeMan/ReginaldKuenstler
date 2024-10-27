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
    @State var selectedTab: Int = 1
    var body: some View {
        TabView(selection:  $selectedTab) {
            UserPaletteView()
                .tag(0)
                .tabItem {
                    Image(systemName: "paintpalette.fill")
                        .renderingMode(.template)
                        .foregroundColor(.red) // <2>
                    Text("Your Palette")
                }
            
            ColourComparisonView()
                .tag(1)
                .tabItem {
                    Image(systemName: "chart.bar.fill")
                        .renderingMode(.template)
                    Text("Analyzer")
                }
            
            MessageView()
                .tag(2)
                .tabItem {
                    Image(systemName: "person.fill.questionmark")
                    Text("TO YOU")
                }
        }
        .tint(.indigo)
    }
}

#Preview {
    ReginaldKuenstlerTabView()
}
