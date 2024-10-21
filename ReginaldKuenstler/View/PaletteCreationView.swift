//
//  PaletteCreationView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

import SwiftUI

struct PaletteColourSelectItem {
    var paletteColour: PaletteColour
    var isSelected: Bool
}

struct PaletteCreationView: View {
    @ObservedObject var viewModel: CreateUserPaletteViewModel = CreateUserPaletteViewModel()
    
    // MARK: Search logic
    @State private var searchText: String = ""
    
    // Grid layout with 3 columns
    let columns = Array(repeating: GridItem(.flexible()), count: 3)
    
    var body: some View {
        NavigationStack {
            VStack {
                ScrollView {
                    // Display colours in a LazyVGrid
                    LazyVGrid(columns: columns, spacing: 16) {
                        // We need indices because of the `isSelected` logic
                        // crashes if we don't have this if statement lmfao what a joke
                        if !viewModel.filteredPaletteColours.isEmpty {
                            ForEach(viewModel.filteredPaletteColours.indices, id: \.self) { index in
                                ColourGridItemView(colourItem: $viewModel.filteredPaletteColours[index])
                                .onTapGesture {
                                    let currentColour = viewModel.filteredPaletteColours[index]
                                    if !currentColour.paletteColour.isUserOwned {
                                        viewModel.filteredPaletteColours[index].paletteColour.toggleIsUserOwned()
                                        
                                        viewModel.filteredPaletteColours[index].isSelected.toggle()
                                        print("--PaletteCreationView, current colour is not owned. Toggled.")
                                    } else {
                                        print("--PaletteCreationView, current colour is already user owned. Not toggling.")
                                    }
                                   
                                    print("--PaletteCreationView, inside onTapGesture of GridItem.")
                                    print("--PaletteCreationView, selectedColour is \(viewModel.filteredPaletteColours[index])\n")
                                }
                            }
                        }
                        
                    }
                    .padding()
                    .scrollContentBackground(.hidden)
                    .searchable(text: $searchText)
                    .onChange(of: searchText) { search in
                        if !search.isEmpty {
                            self.viewModel.filterPaletteColours(term: search)
                        } else {
                            self.viewModel.resetFilteredPaletteColours()
                        }
                    }
                    
                    Spacer()
                    // Button to save selected colours to UserDefaults
                    Group {
                        Button(action: {
                            viewModel.saveSelectedToUserDefaults()
                        }) {
                            Text("Save Selected Colours")
                                .padding()
                                .background(Color.blue)
                                .foregroundColor(.white)
                                .cornerRadius(8)
                        }
                        
                        Spacer()
                         .frame(height:50)
                    }
                    // .frame(maxHeight: .infinity, alignment: .bottom)
                    // end of group
                    
                }
                // end of scrollview
            }
        }
    }
}
